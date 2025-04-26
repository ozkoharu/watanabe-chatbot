from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

"""
## VectorStoreへのナレッジの登録
1. 職務経歴書を文字列として読み込む
2. 職務経歴書の内容（文字列）を特定の文字数でチャンクに分割する
3. Embeddingモデルを用いて、上記のチャンクの文字列をベクトル化する
4. VectorStoreにベクトルの値と文字情報を保存する

## VectorStoreからナレッジの検索
1. 検索をしたいクエリ文字列をEmbeddingモデルを用いてベクトル化する
2. VectorStore上のチャンク情報とクエリ文字列のベクトルを比較して類似度が最も高いチャンクを取得する
  - 類似度の計算アルゴリズム
    - ユークリッド距離
    - コサイン類似度

## 単語
- VectorStore: ベクトルを保存してベクトルで検索できるデータベース
- チャンク: VectorStoreに登録する情報の単位
- Embeddingモデル: 文字列をベクトル化するモデル
"""


class WatanabeKnowledge:
    def __init__(self):
        loader = TextLoader("/var/www/src/app/files/profile.md", encoding="utf-8")
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        docs = text_splitter.split_documents(documents)

        # 文字列をベクトル化するモデルを作成
        embeddings = OpenAIEmbeddings()
        # ベクトルDBにEmbeddingモデルを設定
        self.vector_store = InMemoryVectorStore(embeddings)
        # チャンクに分割されたドキュメントをベクトル化して、ベクトルDBに保存
        self.vector_store.add_documents(documents=docs)

    def search(self, query: str, top_k: int = 1) -> str:
        """
        クエリ文字列と類似度が最も高い外部知識を取得する
        """
        results = self.vector_store.similarity_search(query=query, k=top_k)
        rag_result = ""
        for chunk in results:
            print(f"* {chunk.page_content} [{chunk.metadata}]")
            rag_result = chunk.page_content

        return rag_result
