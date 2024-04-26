import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserDelete(BaseCase):
    def test_delete_user_by_id_2(self):
        # Login with user 2 credentials
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # Try to delete user with ID 2
        response3 = requests.delete(f'https://playground.learnqa.ru/api/user/2',
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid})

        # Assert that the user cannot be deleted
        Assertions.assert_code_status(response3, 400)  # or another error code

    def test_delete_created_user(self):
        # Create a new user
        register_data = self.prepare_registration_data()
        response1 = requests.post('https://playground.learnqa.ru/api/user/', data=register_data)
        user_id = self.get_json_value(response1, 'id')

        # Login with the new user credentials
        login_data = {
            'email': register_data['email'],
            'password': register_data['password']
        }
        response2 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # Delete the user
        response3 = requests.delete(f'https://playground.learnqa.ru/api/user/{user_id}',
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid})

        # Assert that the user is deleted
        Assertions.assert_code_status(response3, 200)

        # Try to get the user data after deletion
        response4 = requests.get(f'https://playground.learnqa.ru/api/user/{user_id}',
                              headers={'x-csrf-token': token},
                              cookies={'auth_sid': auth_sid})

        # Assert that the user data is not available
        Assertions.assert_code_status(response4, 404)  # or another error code

    def test_delete_user_by_id_as_another_user(self):
        # Create a new user
        register_data = self.prepare_registration_data()
        response1 = requests.post('https://playground.learnqa.ru/api/user/', data=register_data)
        user_id = self.get_json_value(response1, 'id')

        # Login with another user credentials
        login_data = {
            'email': 'another_user@example.com',
            'password': '1234'
        }
        response2 = requests.post('https://playground.learnqa.ru/api/user/login', data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, 'x-csrf-token')

        # Try to delete the user
        response3 = requests.delete(f'https://playground.learnqa.ru/api/user/{user_id}',
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid})

        # Assert that the user cannot be deleted
        Assertions.assert_code_status(response3, 400)  # or another error code