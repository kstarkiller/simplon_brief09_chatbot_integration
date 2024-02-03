import json
import requests
from fastapi import FastAPI
import uvicorn

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA5ZTFhOTMtMjZhYi00NTY3LTliODItZDk2NTk4YmNhODIyIiwidHlwZSI6ImFwaV90b2tlbiJ9.IP0_jpdfxZPAhu6R7bT64EPEXNWz2uml2YX6nzSY61I"}
provider = "openai"
url = "https://api.edenai.run/v2/text/chat"

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
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
        "chatbot_global_action": "You are an helpful yet friendly assistant who don't hesitate to tell when you don't know",
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