from models.project import Project
from database import create_session

class ProjectService:
    """
    プロジェクトサービスクラスです。

    プロジェクトの作成、取得、更新、削除などの操作を提供します。
    """

    def __init__(self):
        self.session = create_session()

    def create_project(self, project):
        """
        プロジェクトを作成します。

        Parameters:
            project (Project): 作成するプロジェクトのオブジェクト

        Returns:
            None
        """
        self.session.add(project)
        self.session.commit()

    def get_project(self, id):
        """
        指定されたIDのプロジェクトを取得します。

        Parameters:
            id (int): 取得するプロジェクトのID

        Returns:
            Project: 取得したプロジェクトのオブジェクト
        """
        project = self.session.query(Project).get(id)
        return project
    
    def get_all_projects(self):
        """
        全てのプロジェクトを取得します。

        Returns:
            List[Project]: 全てのプロジェクトのリスト
        """
        projects = self.session.query(Project).all()
        return projects

    def update_project(self, id, updated_project):
        """
        指定されたIDのプロジェクトを更新します。

        Parameters:
            id (int): 更新するプロジェクトのID
            updated_project (dict): 更新するプロジェクトの情報が格納された辞書

        Returns:
            None
        """
        project = self.session.query(Project).get(id)
        for key, value in updated_project.items():
            setattr(project, key, value)
        self.session.commit()

    def delete_project(self, id):
        """
        指定されたIDのプロジェクトを削除します。

        Parameters:
            id (int): 削除するプロジェクトのID

        Returns:
            None
        """
        project = self.session.query(Project).get(id)
        self.session.delete(project)
        self.session.commit()