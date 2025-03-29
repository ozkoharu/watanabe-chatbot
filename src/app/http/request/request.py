from pydantic import BaseModel


class Message(BaseModel):
    text: str


class RequestData(BaseModel):
    message: str
