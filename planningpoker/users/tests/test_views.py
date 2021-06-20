from .test_setup import TestSetUp
from rest_framework.test import force_authenticate
from .factories import UserFactory


class TestViews(TestSetUp):
    def test_user_can_not_register_without_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["email"], "first.last@test.com")
        self.assertEqual(response.data["first_name"], "First")
        self.assertEqual(response.data["last_name"], "Last")
        self.assertEqual(response.data["initials"], "FL")

    def test_user_can_not_login_without_correct_credentials(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_login(self):
        self.client.post(self.register_url, self.user_data)
        data = {
            "email": self.user_data["email"],
            "password": self.user_data["password"],
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_can_refresh_token(self):
        self.client.post(self.register_url, self.user_data)
        data = {
            "email": self.user_data["email"],
            "password": self.user_data["password"],
        }
        obtain_token_response = self.client.post(self.login_url, data)
        refresh_token = obtain_token_response.data["refresh"]
        response = self.client.post(self.refresh_token_url, {"refresh": refresh_token})
        self.assertEqual(response.status_code, 200)

    def test_user_can_not_refresh_same_token_twice(self):
        self.client.post(self.register_url, self.user_data)
        data = {
            "email": self.user_data["email"],
            "password": self.user_data["password"],
        }
        obtain_token_response = self.client.post(self.login_url, data)
        refresh_token = obtain_token_response.data["refresh"]
        first_refresh_response = self.client.post(
            self.refresh_token_url, {"refresh": refresh_token}
        )
        second_refresh_response = self.client.post(
            self.refresh_token_url, {"refresh": refresh_token}
        )
        self.assertEqual(first_refresh_response.status_code, 200)
        self.assertEqual(second_refresh_response.status_code, 401)
