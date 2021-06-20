from rest_framework.test import APITestCase
from django.urls import reverse
from users.tests.factories import UserFactory

class TestSetUp(APITestCase):
    def setUp(self):
        self.project_list_url = reverse("project-list")

        self.user = UserFactory.create_test_user()
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
