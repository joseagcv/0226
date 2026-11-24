# main.py
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import os

class Message(BaseModel):
    message: str

path = os.environ.get('DIRECTORY', "./messages")
file_name= os.environ.get('FILE', "filemessages.txt")
full_path= path + "/" + file_name

list = []

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/messages")
async def add_message():
    f = open(full_path, "r")
    return f.read()

@app.post("/messages")
async def add_message(item: Message):
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(full_path, "a")
    f.write(item.message +"\n")
    f.close


    return item

@app.post("/messages/inmemory")
async def add_message(item: Message):

    list.append(item.message +"\n")
    return item

@app.get("/messages/inmemory")
async def add_message():
    return list


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")