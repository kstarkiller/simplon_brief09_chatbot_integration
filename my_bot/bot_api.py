from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import requests

def pull_model(model_name):
    url = "http://kev-chatbot.westeurope.azurecontainer.io:11434/api/pull"

    data = {"name": model_name, "insecure": True, "stream": False}
    response = requests.post(url, data=json.dumps(data))

    try:
        if response.status_code == 200:
            print("Model is being pulled...")
            progress = response.json()
            while progress["status"] != "success":
                print(f"Progress: {progress['progress']}%")
                response = requests.get(url)
                progress = response.json()
            print("Model is pulled")
        else:
            print("Failed to pull the model")
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    return response.json()   


is_pulled = pull_model("phi3")

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

@app.post("/chatbot")
async def bot_request(request: Request):
    data = await request.json()
    try:
        url = "http://kev-chatbot.westeurope.azurecontainer.io:11434/api/chat"
        response = requests.post(url, json=data)
        result = response.json()

        return result
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Run the API with uvicorn on port 8000
# uvicorn.run(app, host="0.0.0.0", port=8000) 