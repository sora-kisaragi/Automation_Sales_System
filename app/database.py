# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

def create_session():
    # .envファイルからデータベース接続情報を取得
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    dbname = os.getenv('DB_NAME')

    # データベースエンジンを作成
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}')

    # セッションメーカーを作成
    Session = sessionmaker(bind=engine)

    # セッションを作成
    session = Session()

    return session