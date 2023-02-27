import os
from flask import Flask, request, jsonify
import json
# from models.gpt3qa import qa
from flask_cors import CORS
from backend.server.kafka_python.kafka_wrapper import put_messages, get_messages

app = Flask(__name__)
CORS(app)

# @app.route('/', methods=['POST'])
# def home():
#     req = json.loads(request.data)["text"]
#     resp = qa.answer(req)
#     return jsonify({"response": resp})

@app.route('/put-kafka', methods=['POST'])
def put_kafka():
    req = json.loads(request.data)["text"]
    resp = put_messages(message=req)
    return jsonify({"response": "put message"})

@app.route('/get-kafka', methods=['GET'])
def get_kafka():
    resp = get_messages()
    return jsonify({"response": resp})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', os.environ.get('FLASK_PORT')))
    app.run(debug=True, host='0.0.0.0', port=port)
