import pickle
import numpy as np
import openai
import pandas as pd
import tiktoken
import os
import json
import sys

def vector_similarity(x: list[float], y: list[float]) -> float:
    """
    Returns the similarity between two vectors.
    
    Because OpenAI Embeddings are normalized to length 1, the cosine similarity is the same as the dot product.
    """
    return np.dot(np.array(x), np.array(y))

def order_document_sections_by_query_similarity(query: str, contexts: dict[(str, str), np.array], embedding_model: str) -> list[(float, (str, str))]:
    """
    Find the query embedding for the supplied query, and compare it against all of the pre-calculated document embeddings
    to find the most relevant sections. 
    
    Return the list of document sections, sorted by relevance in descending order.
    """
    query_embedding = get_embedding(query, embedding_model)
    
    document_similarities = sorted([
        (vector_similarity(query_embedding, doc_embedding), doc_index) for doc_index, doc_embedding in contexts.items()
    ], reverse=True)
    
    return document_similarities

def construct_prompt(question, context_embeddings, df, separator_len, MAX_SECTION_LEN, SEPARATOR, EMBEDDING_MODEL) -> str:
    """
    Fetch relevant 
    """
    most_relevant_document_sections = order_document_sections_by_query_similarity(question, context_embeddings, EMBEDDING_MODEL)
    
    chosen_sections = []
    chosen_sections_len = 0
    chosen_sections_indexes = []
     
    for _, section_index in most_relevant_document_sections:
        # Add contexts until we run out of space.        
        document_section = df.loc[section_index]
        
        chosen_sections_len += document_section.tokens + separator_len
        if chosen_sections_len > MAX_SECTION_LEN:
            break
            
        chosen_sections.append(SEPARATOR + document_section.content.replace("\n", " "))
        chosen_sections_indexes.append(str(section_index))
            
    # Useful diagnostic information
    print(f"Selected {len(chosen_sections)} document sections:")
    print("\n".join(chosen_sections_indexes))
    
    header = """Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text below, say "I don't know."\n\nContext:\n"""
    
    return header + "".join(chosen_sections) + "\n\n Q: " + question + "\n A:"

def answer_query_with_context(
    query,
    df,
    document_embeddings,
    show_prompt,
    separator_len, 
    MAX_SECTION_LEN, 
    SEPARATOR,
    COMPLETIONS_MODEL,
    EMBEDDING_MODEL) -> str:

    prompt = construct_prompt(
        query,
        document_embeddings,
        df,
        separator_len,
        MAX_SECTION_LEN,
        SEPARATOR,
        EMBEDDING_MODEL
    )
    
    if show_prompt:
        print(prompt)
        
    COMPLETIONS_API_PARAMS = {
    # We use temperature of 0.0 because it gives the most predictable, factual answer.
    "temperature": 0.0,
    "max_tokens": 300,
    "model": COMPLETIONS_MODEL,
    }

    response = openai.Completion.create(
                prompt=prompt,
                **COMPLETIONS_API_PARAMS
            )

    return response["choices"][0]["text"].strip(" \n")

def get_embedding(text: str, model: str) -> list[float]:

    result = openai.Embedding.create(
      model=model,
      input=text
    )
    return result["data"][0]["embedding"]

def search(query, COMPLETIONS_MODEL, EMBEDDING_MODEL, df):

    # with open('./models/gpt3qa/data/document_embeddings.pickle', 'rb') as handle:
    with open('./data/document_embeddings.pickle', 'rb') as handle:
        document_embeddings = pickle.load(handle)

    MAX_SECTION_LEN = 500
    SEPARATOR = "\n* "
    ENCODING = "cl100k_base"  # encoding for text-embedding-ada-002

    encoding = tiktoken.get_encoding(ENCODING)
    separator_len = len(encoding.encode(SEPARATOR))

    prompt = construct_prompt(
        query,
        document_embeddings,
        df,
        separator_len,
        MAX_SECTION_LEN,
        SEPARATOR,
        EMBEDDING_MODEL
    )

    COMPLETIONS_API_PARAMS = {
    # We use temperature of 0.0 because it gives the most predictable, factual answer.
    "temperature": 0.0,
    "max_tokens": 300,
    "model": COMPLETIONS_MODEL,
    }

    return answer_query_with_context(query, df, document_embeddings, False, separator_len, MAX_SECTION_LEN, SEPARATOR, COMPLETIONS_MODEL, EMBEDDING_MODEL)

def answer(text: str):

    COMPLETIONS_MODEL = "text-davinci-003"
    EMBEDDING_MODEL = "text-embedding-ada-002"

    openai.api_key = os.environ['OPENAI_API_KEY']

    prompt = "are structured settlements taxed"

    # df = pd.read_csv('./models/gpt3qa/data/wikipedia-ss.csv')
    df = pd.read_csv('./data/wikipedia-ss.csv')

    df = df.set_index(["title", "heading"])

    return search(text, COMPLETIONS_MODEL, EMBEDDING_MODEL, df)