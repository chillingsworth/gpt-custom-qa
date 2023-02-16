import os
from flask import Flask, request, jsonify
import json
from models.gpt3qa import qa
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def home():
    req = json.loads(request.data)["text"]
    resp = qa.answer(req)
    return jsonify({"response": resp})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', os.environ.get('FLASK_PORT')))
    app.run(debug=True, host='0.0.0.0', port=port)
