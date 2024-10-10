import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime

app = FastAPI()
messages = []
likes = {}


class Message(BaseModel):
    username: str
    content: str


USER_SERVICE_URL = "http://127.0.0.1:8001"


@app.post("/post")
def post_message(message: Message):
    if len(message.content) > 400:
        raise HTTPException(status_code=400, detail="Message exceeds 400 characters")

    response = requests.get(f"{USER_SERVICE_URL}/users/{message.username}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="User is not registered")

    message_entry = {
        "username": message.username,
        "content": message.content,
        "timestamp": datetime.datetime.utcnow(),
        "likes": 0
    }
    messages.append(message_entry)
    return {"message": "Message posted successfully"}


@app.get("/messages")
def get_messages():
    return messages


@app.post("/like")
def like_message(message: Message):
    response = requests.get(f"{USER_SERVICE_URL}/users/{message.username}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="User is not registered")

    message_id = int(message.content)
    if message_id < 0 or message_id >= len(messages):
        raise HTTPException(status_code=404, detail="Message not found")
    messages[message_id]["likes"] += 1
    return {"message": "Message liked successfully"}
