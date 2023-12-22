from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel
from openai import OpenAI, ChatCompletion
from dotenv import load_dotenv
import os

router = APIRouter()

@router.post("/chat")
async def chat_gpt(message: ChatMessage):
    """
    メッセージをChatGPTに送信し、返答を返します。

    Parameters:
        message (ChatMessage): メッセージ

    Returns:
        str: ChatGPTからの返答
    """
    # ここでChatGPTにメッセージを送信し、返答を取得します。
    # 注意: 実際のコードでは、OpenAIのAPIキーとその他の設定が必要です。
    # 以下のコードは例示的なもので、実際には動作しません。
    openai = OpenAI("your-api-key")
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
    * 1つのメール本文に複数案件がある場合は一回の出力にまとめてください
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
            }
        ]
    }
    """
    chat = ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": default_message}, {"role": "user", "content": message.message}])
    return chat['choices'][0]['message']['content']

@router.post("/count_tokens")
async def count_tokens(message: ChatMessage):
    """
    メッセージのトークン数を計算します。

    Parameters:
        message (ChatMessage): メッセージ

    Returns:
        int: トークン数
    """
    # ここでメッセージのトークン数を計算します。
    # 注意: 実際のコードでは、OpenAIのAPIキーとその他の設定が必要です。
    # 以下のコードは例示的なもので、実際には動作しません。
    openai = OpenAI("your-api-key")
    tokens = openai.count_tokens(message.message)
    return tokens