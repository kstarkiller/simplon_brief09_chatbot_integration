# import sys
# import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import requests
from bs4 import BeautifulSoup

# sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
# from hidden import B09_API_KEY

# Set the API key and the headers
headers = {"Authorization": "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA5ZTFhOTMtMjZhYi00NTY3LTliODItZDk2NTk4YmNhODIyIiwidHlwZSI6ImFwaV90b2tlbiJ9.IP0_jpdfxZPAhu6R7bT64EPEXNWz2uml2YX6nzSY61I"} # Replace B09_API_KEY with your own API key
provider = "meta"
url = "https://api.edenai.run/v2/text/chat"

# Scraping all the text of my website and remove the leading and trailing whitespaces with strip()
# response = requests.get("http://localhost:8001")
# soup = BeautifulSoup(response.content, "html.parser")

app = FastAPI()

# Allow CORS
origins = ["*"]
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
    # site_content = soup.get_text().strip()

    payload = {
        "providers": provider,
        "text": "",
        # "chatbot_global_action": f"You are not an assistant. You are Kevin, the owner of the website of which here is the content : {site_content}",
        "chatbot_global_action": "You are an helpful yet too friendly assistant",
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

# Run the API with uvicorn on port 8000
uvicorn.run(app, host="0.0.0.0", port=8000)