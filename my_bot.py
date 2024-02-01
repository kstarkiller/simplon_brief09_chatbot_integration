import json
import requests

def bot_request(provider, url, headers):
    payload = {
        "providers": provider,
        "text": "",
        "chatbot_global_action": "You are an helpful yet friendly assistant",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": ""
    }

    while True:
        prompt = input(f"-------\nDis-moi quelque chose : ")

        if prompt in ["quit", "logout", "exit", "bye"] :
            break

        payload['text'] = prompt

        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)[provider]

        payload['previous_history'].append(result['message'][0])
        payload['previous_history'].append(result['message'][1])

        print(f"\nMa réponse: {result['generated_text']} \n\nCoût de cet échange: {result['cost']}\n")