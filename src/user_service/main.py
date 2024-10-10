from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = set()

class User(BaseModel):
    username: str

@app.post("/register")
def register_user(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    users.add(user.username)
    return {"message": "User registered successfully"}

@app.get("/users/{username}")
def get_user(username: str):
    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": username}
