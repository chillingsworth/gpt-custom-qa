import pickle
import numpy as np
import openai
import pandas as pd
import tiktoken
import os
import json

def call():
    with open('./models/gpt3qa/data/document_embeddings.pickle', 'rb') as handle:
        document_embeddings = pickle.load(handle)
    return "test"


def test(text: str):

    call()
    # return {'status': 200, 'dir': str([x[0] for x in os.walk(os.getcwd())])}
    openai.api_key = os.environ['OPENAI_API_KEY']

    prompt = "are structured settlements taxed"

    df = pd.read_csv('./models/gpt3qa/data/wikipedia-ss.csv')

    return {'status': 200, 'dir': str(os.environ['OPENAI_API_KEY'])}
