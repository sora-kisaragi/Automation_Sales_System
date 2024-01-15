# database.py
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    """
    データベース接続とセッション管理を行うクラス。
    SQLAlchemyを使用してORM機能を提供します。
    """

    def __init__(self):
        """
        コンストラクタ。環境変数からデータベース接続情報を読み込み、
        エンジンとセッションの初期化を行います。
        """
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.dbname = os.getenv('DB_NAME')
        self.engine = None
        self.session = None

    def create_engine(self):
        """
        データベースエンジンを作成します。
        """
        connection_string = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}'
        self.engine = create_engine(connection_string)
    
    def get_engine(self):
        """
        データベースエンジンのインスタンスを取得します。
        エンジンがまだ初期化されていない場合は初期化を行います。
        """
        if not self.engine:
            self.create_engine()
        return self.engine
    
    def create_session(self):
        """
        新しいセッションを作成し、それを返します。
        エンジンがまだ作成されていない場合は、先にエンジンを作成します。

        :return: 新しいセッションオブジェクト
        """
        if not self.engine:
            self.create_engine()
        Session = scoped_session(sessionmaker(bind=self.engine, autocommit=False, autoflush=False))
        self.session = Session()
        return self.session

    def close_session(self):
        """
        アクティブなセッションがあれば閉じます。
        """
        if self.session:
            self.session.close()

    def begin_transaction(self):
        """
        新しいトランザクションを開始します。

        :return: トランザクションオブジェクト
        """
        return self.session.begin()

    def commit(self):
        """
        現在のトランザクションをコミットします。
        """
        self.session.commit()

    def rollback(self):
        """
        現在のトランザクションをロールバックします。
        """
        self.session.rollback()

    def create_tables(self, base):
        """
        モデルからデータベーステーブルを作成します。

        :param base: SQLAlchemyのBaseメタデータオブジェクト
        """
        base.metadata.create_all(self.engine)

    def drop_tables(self, base):
        """
        データベースから全てのテーブルを削除します。

        :param base: SQLAlchemyのBaseメタデータオブジェクト
        """
        base.metadata.drop_all(self.engine)

    def initialize_database(self, base, initial_data_function=None):
        """
        データベースを初期化します。既存のテーブルを削除し、新しいテーブルを作成します。
        初期データを挿入するための関数が提供されている場合は、その関数を実行します。

        :param base: SQLAlchemyのBaseメタデータオブジェクト
        :param initial_data_function: 初期データを挿入するための関数（オプション）
        """
        self.drop_tables(base)
        self.create_tables(base)
        if initial_data_function:
            initial_data_function(self.session)
            
    def test_connection(self):
        """
        データベースへの接続をテストします。
        接続が成功すれば True を、失敗すれば False を返します。
        """
        try:
            # エンジンが定義されていない場合は、エンジンを作成します。
            if not self.engine:
                self.create_engine()
            # text() 関数を使用してSQLステートメントを実行します。
            with self.engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                return True
        except Exception as e:
            print(f"接続テスト中にエラーが発生しました: {e}")
            return False