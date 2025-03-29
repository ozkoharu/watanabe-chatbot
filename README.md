# watanabe-chatbot

### .envファイルの作成

以下のコマンドでローカル開発環境用の.envファイルを作成します。

```

cp environment/local/.env.example environment/local/.env

```

### コンテナの立ち上げ

以下のコマンドでローカル開発環境用のコンテナを立ち上げます。

```

bash dev.bash up

```

## 作るもの

- RAGを活用したチャットbotAPI
- 職務経歴書の情報をRAGにいれて、渡邊くんのことを回答してくれるチャットbot

### 使用する技術

- 言語：python
- APIフレームワーク：FastAPI
- LLMフレームワーク：LangChain
- VectorDB：OpenSearch

### API仕様

エンドポイント：`localhost:任意のport/api/v1/chat`

HTTPメソッド：`POST`

#### ヘッダー

```

{

    "Content-Type": "application/json"

}

```

#### Body

```

{

    "message": "こんにちは"

}

```

#### Response

```

{

    "answer": "さようなら"

}

```
