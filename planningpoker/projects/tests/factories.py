from common.obfuscater import Obfuscater
from projects.models import Project, ProjectMember
from users.tests.factories import UserFactory


class ProjectFactory:
    @classmethod
    def create_project(cls, *args, **kwargs):
        return Project.objects.create_project(*args, **kwargs)

    @classmethod
    def create_test_project(cls, user=None):
        user = user or UserFactory.create_test_user()
        title = Obfuscater.project_title()
        return cls.create_project(title=title, user=user)
