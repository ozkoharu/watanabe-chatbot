from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI

from app.objects.watanabe_knowledge import WatanabeKnowledge

SYSTEM_PROMPT = """
あなたはわたなべゆうたに関する情報に回答するチャットbotです。
- 応答は必ず{lang}で返してください

## RAGで取得したプロフィール情報
{profile}
"""


class ChatUseCase:
    def chat(self, message) -> str:
        """
        ユーザーメッセージを受け取って渡邊雄太に関する情報を用いて回答を生成する
        """
        # 外部知識を取得する
        watanabe_knowledge = WatanabeKnowledge()
        rag_result = watanabe_knowledge.search(message)
        # モデル定義
        llm = ChatOpenAI(model="gpt-4o")
        # プロンプト作成
        prompt_template = ChatPromptTemplate.from_messages(
            [
                # システム部
                SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT),
                # ユーザー部
                HumanMessagePromptTemplate.from_template(message),
            ]
        )
        # プロンプトテンプレートを使ってLLMを呼び出す
        chain = prompt_template | llm
        response = chain.invoke({"lang": "日本語", "profile": rag_result})
        return response.content
