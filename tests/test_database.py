# test_database.py
import unittest
from src.database import Database
from sqlalchemy.orm import Session
from src.models.base import Base  # 共通の Base インスタンスをインポート
from src.models.project import Project
from src.models.skill import Skill
from src.models.company import Company
from src.models.contact import Contact
from src.models.project_skill import ProjectSkill

class TestDatabase(unittest.TestCase):
    """
    Databaseクラスのテストケース。
    """

    def setUp(self):
        """
        各テストメソッドの実行前にデータベース接続とセッションを設定し、
        トランザクションを開始します。
        """
        self.database = Database()
        self.session = self.database.create_session()
        self.transaction = self.database.begin_transaction()  # トランザクションを開始

    def tearDown(self):
        """
        各テストメソッドの実行後にトランザクションをロールバックし、
        セッションを閉じます。
        """
        try:
            self.database.rollback()  # トランザクションをロールバック
        except Exception as e:
            print(f"ロールバック中にエラーが発生しました: {e}")
        finally:
            self.database.close_session()

    def test_create_session(self):
        """
        create_sessionメソッドがSessionインスタンスを正しく生成することをテストします。
        """
        self.assertIsInstance(self.session, Session, "生成されたセッションがSessionクラスのインスタンスではありません。")

    def test_connection(self):
        """
        データベースへの接続が正しく行われることをテストします。
        """
        self.assertTrue(self.database.test_connection(), "データベースへの接続テストに失敗しました。")

    def test_drop_tables(self):
        """
        drop_tablesメソッドがテーブルを正しく削除することをテストします。
        """
        # テーブルを作成し、その後で削除をテストします。
        self.database.create_tables(Base)
        self.database.drop_tables(Base)
        engine = self.database.get_engine()
        metadata = Base.metadata
        metadata.clear()
        metadata.reflect(bind=engine)
        for model in [Company, Contact, ProjectSkill, Skill, Project]:
            self.assertNotIn(model.__tablename__, metadata.tables, f"{model.__tablename__} テーブルが削除されていません。")

    def test_create_tables(self):
        """
        create_tablesメソッドがテーブルを正しく作成することをテストします。
        """
        # 既存のテーブルを削除します。
        self.database.drop_tables(Base)
        # テーブルを作成します。
        self.database.create_tables(Base)
        engine = self.database.get_engine()
        # テーブルが存在するかどうかを確認するためにメタデータを使用します。
        metadata = Base.metadata
        metadata.reflect(bind=engine)
        for model in [Company, Contact, ProjectSkill, Skill, Project]:
            self.assertIn(model.__tablename__, metadata.tables, f"{model.__tablename__} テーブルが作成されていません。")


if __name__ == '__main__':
    unittest.main()