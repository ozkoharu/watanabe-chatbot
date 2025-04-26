from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.http.contoroller.llm_controller import LLMController
from app.http.request.request import Message, RequestData

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "OK"}


@router.post("/kon")
def response_msg(msg: Message):
    """
    ヘルスチェック用
    """
    if msg.text == "こんにちは":
        return {"response": "さよなら"}
    return JSONResponse(content={"resonse": "不明なメッセージ"})


@router.post("/llm/chat")
def response_name(request: RequestData):
    """
    チャット用
    """
    controller = LLMController()
    return controller.generate_response(request)
