import os

from langchain_openai import OpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

llm = OpenAI()

prompt_template = ChatPromptTemplate.from_messages([
    # システム部
    SystemMessage(content='You are a helpful assistant, 応答は日本語で返してください'),
    # ユーザー部
    HumanMessagePromptTemplate.from_template("Call me {name}")
])

# このプロンプトテンプレートを使ってLLMを呼び出す
chain = prompt_template | llm
response = chain.invoke({"name": "太郎"})
print(response)
