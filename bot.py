# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
from flask import Flask, request, jsonify

CORPUS_FILE = "chat.txt"
chatbot = ChatBot("Chatbot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

app = Flask(__name__)


def set_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'  # Allow specific HTTP methods
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response


@app.route('/conversation', methods=['POST', 'OPTIONS'])
def post_data():
    if request.method == 'OPTIONS':
        # Handle preflight CORS requests
        response = jsonify({'message': 'CORS preflight request handled'})
        response = set_cors_headers(response)
        return response

    data = request.get_json()
    response = jsonify({'message': f"{chatbot.get_response(data['message'])}"})
    response = set_cors_headers(response)
    return response


if __name__ == '__main__':
    app.run()
