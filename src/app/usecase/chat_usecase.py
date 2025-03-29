from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI


class ChatUseCase:
    def chat(self, message) -> str:
        loader = TextLoader("/var/www/src/app/files/profile.md", encoding="utf-8")
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        docs = text_splitter.split_documents(documents)

        # 文字列をベクトル化するモデルを作成
        embeddings = OpenAIEmbeddings()
        # ベクトルDBにEmbeddingモデルを設定
        vector_store = InMemoryVectorStore(embeddings)
        # チャンクに分割されたドキュメントをベクトル化して、ベクトルDBに保存
        vector_store.add_documents(documents=docs)
        # 類似度検索を実行
        # k: 上位n件取得
        results = vector_store.similarity_search(query=message, k=1)
        rag_result = ""
        for chunk in results:
            print(f"* {chunk.page_content} [{chunk.metadata}]")
            rag_result = chunk.page_content

        llm = ChatOpenAI(model="gpt-4o")

        system_prompt = """
あなたはわたなべゆうたに関する情報に回答するチャットbotです。
- 応答は必ず{lang}で返してください

## RAGで取得したプロフィール情報
{profile}
"""

        prompt_template = ChatPromptTemplate.from_messages(
            [
                # システム部
                SystemMessagePromptTemplate.from_template(system_prompt),
                # ユーザー部
                HumanMessagePromptTemplate.from_template(message),
            ]
        )

        # このプロンプトテンプレートを使ってLLMを呼び出す
        chain = prompt_template | llm
        response = chain.invoke({"lang": "日本語", "profile": rag_result})
        return response.content
