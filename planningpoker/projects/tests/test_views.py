from projects.models import Project, ProjectMember
from rest_framework.test import force_authenticate

from .factories import ProjectFactory
from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_anon_user_can_not_create_project(self):
        response = self.client.post(self.project_list_url)
        self.assertEqual(response.status_code, 401)

    def test_user_can_not_create_project_without_data(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.project_list_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_create_project(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Test Project",
        }
        response = self.client.post(self.project_list_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], data["title"])

    def test_user_added_as_owner_on_project_create(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Test Project",
        }
        response = self.client.post(self.project_list_url, data)
        project_id = response.data["id"]
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            ProjectMember.objects.filter(
                project__id=project_id, user=self.user
            ).count(),
            1,
        )

    def test_anon_user_can_not_get_list_of_projects(self):
        ProjectFactory.create_test_project(self.user)
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, 401)

    def test_user_can_get_list_of_projects_no_projects(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)

    def test_user_can_get_list_of_projects(self):
        ProjectFactory.create_test_project(self.user)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_user_can_only_get_list_of_projects_it_it_member_of(self):
        project = ProjectFactory.create_test_project(self.user)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

        ProjectMember.objects.get(user=self.user, project__id=project.id).delete()
        response = self.client.get(self.project_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)
