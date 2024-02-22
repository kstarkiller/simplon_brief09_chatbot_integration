from transformers import AutoTokenizer, AutoModelForCausalLM
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests
import uvicorn

import sys
sys.path.append("../../")
from hidden import GEMMA_HF_KEY

# Scraping all the text of my website and remove the leading and trailing whitespaces with strip()
response = requests.get("http://localhost:8001")
soup = BeautifulSoup(response.content, "html.parser")

# Access token here
TOKEN = GEMMA_HF_KEY

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it", use_auth_token=TOKEN)
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it", use_auth_token=TOKEN)

app = FastAPI()

# Allow CORS
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
async def gemma_request(prompt: str):
    site_content = soup.get_text().strip()

    prompt = f"Knowing this :{site_content}, answer this : {prompt}"

    input_ids = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**input_ids, max_new_tokens=20)

    response = tokenizer.decode(outputs[0])

    return {"response": response}

uvicorn.run(app)