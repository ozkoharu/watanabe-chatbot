
from fastapi import FastAPI
from pydantic import  BaseModel

class Message(BaseModel):
    text: str

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'OK'}

@app.post('/kon')
def response_msg(msg: Message):
    if msg.text == "こんにちは":
        return {"response": "さよなら"}
    return {"response" : "不明なメッセージ"}

