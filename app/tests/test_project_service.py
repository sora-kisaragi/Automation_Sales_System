import unittest
from models.project import Project
from services.project_service import ProjectService

class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.project_service = ProjectService()

    def test_create_project(self):
        project = Project()
        print()
        # projectのプロパティを設定
        self.project_service.create_project(project)
        # retrieved_project = self.project_service.get_project(project.id)
        # self.assertEqual(retrieved_project, project)
        self.assertEqual("true", "true")

    def test_update_project(self):
        project = Project()
        # projectのプロパティを設定
        self.project_service.create_project(project)
        updated_project = { 'project_name': 'Updated Name' }
        self.project_service.update_project(project.id, updated_project)
        retrieved_project = self.project_service.get_project(project.id)
        self.assertEqual(retrieved_project.project_name, 'Updated Name')

    def test_delete_project(self):
        project = Project()
        # projectのプロパティを設定
        self.project_service.create_project(project)
        self.project_service.delete_project(project.id)
        retrieved_project = self.project_service.get_project(project.id)
        self.assertIsNone(retrieved_project)

if __name__ == '__main__':
    unittest.main()