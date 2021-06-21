from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")
        self.refresh_token_url = reverse("token_refresh")

        self.user_data = {
            "email": "first.last@test.com",
            "first_name": "First",
            "last_name": "Last",
            "password": "supersecret",
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
