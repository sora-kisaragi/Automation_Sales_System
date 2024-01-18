import os
import uvicorn
from fastapi import FastAPI
from routers import chatgpt
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む

mode = os.getenv("MODE")  # 環境変数MODEを取得

app = FastAPI(
    docs_url=None if mode != "debug" else "/docs",
    redoc_url=None if mode != "debug" else "/redoc",
)

app.include_router(chatgpt.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)