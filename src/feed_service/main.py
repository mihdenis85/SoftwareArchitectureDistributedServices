from fastapi import FastAPI
import requests

app = FastAPI()

MESSAGE_SERVICE_URL = "http://127.0.0.1:8002"

@app.get("/feed")
def get_feed():
    response = requests.get(f"{MESSAGE_SERVICE_URL}/messages")
    if response.status_code == 200:
        messages = response.json()
        return messages[-10:]
    else:
        return {"error": "Unable to fetch messages"}
