from unittest.mock import Mock
import unittest
from models.project import Project
from services.project_service import ProjectService

class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.project_service = ProjectService()
        self.project = Project()
        self.project.project_name = 'Test Project'
        self.project.summary = 'This is a test project'

    def test_create_project(self):
        self.project_service.create_project(self.project)
        retrieved_project = self.project_service.get_project(self.project.id)
        self.assertEqual(retrieved_project, self.project)


    def test_read_project(self):
        """
        get_projectメソッドをテストします。
        """
        # プロジェクトを作成してIDを取得
        self.project_service.create_project(self.project)
        project_id = self.project.id

        # get_projectメソッドを使用してプロジェクトを取得
        retrieved_project = self.project_service.get_project(project_id)

        # 取得したプロジェクトが期待したものであることを確認
        self.assertEqual(retrieved_project.project_name, self.project.project_name)
        self.assertEqual(retrieved_project.summary, self.project.summary)
        
        
    def test_update_project(self):
        updated_project = { 'project_name': 'Updated Name' }
        self.project_service.create_project(self.project)
        self.project_service.update_project(self.project.id, updated_project)
        retrieved_project = self.project_service.get_project(self.project.id)
        self.assertEqual(retrieved_project.project_name, 'Updated Name')

    def test_delete_project(self):
        self.project_service.create_project(self.project)
        self.project_service.delete_project(self.project.id)
        retrieved_project = self.project_service.get_project(self.project.id)
        self.assertIsNone(retrieved_project)
        
    def test_get_all_projects(self):
        # テスト用のプロジェクトデータを作成
        project1 = Project(project_name='Project 1', summary='summary 1')
        project2 = Project(project_name='Project 2', summary='summary 2')

        # モックされたセッションオブジェクトを作成し、query().all() の戻り値を設定
        mock_session = Mock()
        mock_session.query().all.return_value = [project1, project2]

        # プロジェクトサービスのセッションをモックセッションに置き換え
        self.project_service.session = mock_session

        # get_all_projects メソッドを呼び出してプロジェクトリストを取得
        projects = self.project_service.get_all_projects()

        # 取得したプロジェクトリストが期待通りのものかを検証
        self.assertEqual(len(projects), 2)
        self.assertEqual(projects[0].project_name, 'Project 1')
        self.assertEqual(projects[1].summary, 'summary 2')


if __name__ == '__main__':
    unittest.main()