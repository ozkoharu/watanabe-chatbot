from fastapi.responses import JSONResponse

from app.http.request.request import RequestData
from app.usecase.chat_usecase import ChatUseCase


class LLMController:
    def generate_response(self, request: RequestData) -> JSONResponse:
        usecase = ChatUseCase()
        answer = usecase.chat(request.message)
        print(answer)
        return JSONResponse(content={"response": answer})
