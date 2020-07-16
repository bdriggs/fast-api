from fastapi import FastAPI
import json
from pydantic import BaseModel
import uvicorn
import requests


class Users(BaseModel):
    users: dict = {}


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def get_users():
    with open('./data/users/users.json') as users_file:
        users = json.load(users_file)

    return users


@app.put("/users", response_model=Users)
async def post_users(users: Users):
    with open('./data/users/users.json', 'w') as users_file:
        json.dump(users.users, users_file)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
