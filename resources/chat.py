import os
import openai
from dotenv import load_dotenv
import requests

load_dotenv()

openai.organization = "org-6wWesWVaoTDSMfehSqVekHKz"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


from flask import Blueprint, jsonify, request

chat = Blueprint('chat', 'chat')



@chat.route('/', methods=['POST'])
def handle_chatbot_request():
    user_message = request.json['message']
    print(user_message)

    headers = {
        'Authorization': f'Bearer {openai.api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': user_message}]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    
    print(response.json())

    chat_response = response.json()['choices'][0]['message']['content']
    
    return jsonify({
        'data': chat_response,
        'message': "Received a response!",
        'status': 200
    }), 200