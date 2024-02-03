import json
import requests
import sys
sys.path.append("../../")
from hidden import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

headers = {"Authorization": B09_API_KEY}
provider = "openai"
url = "https://api.edenai.run/v2/text/chat"

app = FastAPI()

origins = ["http://localhost", "http://localhost:8001"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)

@app.get("/test/{prompt}")
async def read_item(prompt):
    return {"It works"}

@app.post("/{prompt}")
async def bot_request(prompt):
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

    return result['generated_text']

uvicorn.run(app)