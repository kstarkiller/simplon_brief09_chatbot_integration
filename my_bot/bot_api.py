from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import requests
import ollama
from bs4 import BeautifulSoup

app = FastAPI()

# Allow CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/test/{prompt}")
async def read_item(prompt):
    return {"It works"}

@app.post("/{prompt}")
async def bot_request(prompt):
    # Get the response from the chatbot
    result = ollama.generate(model='llama3', prompt=prompt)

    return result["response"]

# Run the API with uvicorn on port 8000
uvicorn.run(app, host="0.0.0.0", port=8000)