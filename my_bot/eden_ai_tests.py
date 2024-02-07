import json
import requests
import sys
sys.path.append("../../")
from hidden import *

# Set the API key and the headers
headers = {"Authorization": "Bearer " + B09_API_KEY}
provider = "openai"
url = "https://api.edenai.run/v2/text/chat"

# Define a function to get the bot response
def get_bot_response(provider, url, headers):
    prompt = input("Ask my anything : ")
    while prompt not in ["quit", "exit", "end"]:
        payload = {
            "providers": provider,
            "text": "",
            "chatbot_global_action": "You are an helpful, friendly yet respectful assistant and don't hesitate to tell when you don't know",
            "previous_history": [],
            "temperature": 0.0,
            "max_tokens": 150,
            "fallback_providers": ""
        }

        payload['text'] = prompt

        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)[provider]

        payload['previous_history'].append(result['message'][0])
        payload['previous_history'].append(result['message'][1])

        print(result['generated_text'])
        
        prompt = input("Anything else ? : ")

get_bot_response(provider, url, headers)
