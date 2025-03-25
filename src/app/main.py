
from fastapi import FastAPI
from pydantic import  BaseModel
from llms import generate_response

class Message(BaseModel):
    text: str
class RequestData(BaseModel):
    name: str

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'OK'}

@app.post('/kon')
def response_msg(msg: Message):
    if msg.text == "こんにちは":
        return {"response": "さよなら"}
    return {"response" : "不明なメッセージ"}

@app.post('/llm/api')
def response_name(data: RequestData):
    response = generate_response(data.name)
    return {"response": response}
