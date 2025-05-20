from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello whats up!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip().lower()

    if user_message == 'hi':
        reply = 'hello'
    else:
        reply = "I didn't understand that. Try saying 'hi'."

    return jsonify({'reply': reply})
