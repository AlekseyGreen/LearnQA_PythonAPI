import requests
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import pytest

class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    @pytest.mark.parametrize('email', ['invalid_email', 'invalid_email@', 'invalid_email.com'])
    def test_create_user_with_invalid_email(self, email):
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "Invalid email format", f'Unexpected response content: {response.content}'

    @pytest.mark.parametrize('field_to_remove', ['password', 'username', 'firstName', 'lastName', 'email'])
    def test_create_user_without_field(self, field_to_remove):
        data = {
            'password': '123',
            'username': 'learqa',
            'firstName': 'learqa',
            'lastName': 'learqa',
            "email": self.email
        }
        data.pop(field_to_remove)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"The following required params are missed: {field_to_remove}", \
            f'Unexpected response content: {response.content}'

    def test_create_user_with_short_username(self):
        data = {
            'password': '123',
            'username': 'a',
            'firstName': 'learqa',
            'lastName': 'learqa',
            "email": self.email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'username' field is too short", \
            f'Unexpected response content: {response.content}'

    def test_create_user_with_long_username(self):
        long_username = "a" * 251
        data = {
            'password': '123',
            'username': long_username,
            'firstName': 'learqa',
            'lastName': 'learqa',
            "email": self.email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'username' field is too long", \
            f'Unexpected response content: {response.content}'