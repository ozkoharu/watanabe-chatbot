## 環境の初期化

```
poetry init
```

## ライブラリ追加の方法

```
poetry add langchain-openai
poetry add fastapi uvicorn
```

## 参考ページ

- https://note.com/npaka/n/n24d48303a496

## サーバー起動コマンド
```
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
