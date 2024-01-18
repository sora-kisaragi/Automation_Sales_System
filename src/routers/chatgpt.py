from models.chatmessage import ChatMessage
import json
from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import os

load_dotenv()  # .envファイルから環境変数を読み込む
API_KEY = os.getenv("API_KEY")  # APIキーを環境変数から取得

router = APIRouter(prefix="/api/v1")

@router.post("/chat", tags=["chatgpt"])
async def convert_infomation(message: ChatMessage):
    """
    メッセージをChatGPTに送信し、返答を返します。

    Parameters:
        message (ChatMessage): メッセージ

    Returns:
        str: ChatGPTからの返答
    """

    default_message = """
    #命令書
    あなたはSESの営業担当者を補佐する事務員のスペシャリストです。
    案件紹介、案内のメール文面から必要情報を抜き出し
    jsonにして返答してください。

    以下の制約条件を全て満たす返答をしてください。

    ## 制約条件
    * json形式で回答してください
    * jsonの構造は別途下記に記載します
    * 例文を提示するので参考にしてください
    * 存在しない値はnullで回答してください
    * 必ずすべてのkeyを含む状態で生成してください
    * step by step で考えてください
    * メール形式でデータを入力するので不要なものは省いてください
    * 1つのメール本文に複数案件がある場合は配列で出力してください
    * 間違いないか確認してください


    ## Jsonの構造
    {
        "data": [
            {
                "企業名": "string",
                "担当者": "string",
                "案件名": "string",
                "案件内容": "string",
                "勤務地": "string",
                "期間": "string",
                "募集人数": "string",
                "単価要件": "string",
                "精算": "string",
                "必須スキル": [
                    "string"
                ],
                "スキル": [
                    "string"
                ],
                "面談": "string",
                "要約": "string"
            }...
        ]
    }
    """
    client = OpenAI(api_key=API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": default_message},
            {"role": "user", "content": message.message}
        ],
        model="gpt-3.5-turbo",
    )
    try:
        # 応答をJSONとして解析
        response = json.loads(chat_completion.choices[0].message.content)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="処理に失敗しました")
    return response

@router.post("/count_tokens", tags=["chatgpt"])
async def count_tokens(message: ChatMessage):
    """
    メッセージのトークン数を計算します。

    Parameters:
        message (ChatMessage): メッセージ

    Returns:
        int: トークン数
    """
    enc = tiktoken.get_encoding("cl100k_base")
    e = enc.encode(message.message)

    tokens = len(e)
    return tokens