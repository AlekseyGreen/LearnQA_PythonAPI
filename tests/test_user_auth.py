import pytest
import requests
from lib.base_case import BaseCase

class TestUserAuth(BaseCase):
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]
    def setup_method(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post(
            "https://playground.learnqa.ru/api/user/login",
            data=data)

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_from_auth_method = self.get_json_value(response1, 'user_id')

    def test_auth_user(self):
        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid': self.auth_sid},
        )

        assert 'user_id' in response2.json(), "There is no user_id in response2"

        user_id_from_chek_method = response2.json()['user_id']

        assert self.user_id_from_auth_method == user_id_from_chek_method, \
            'user id from auth method in not equal to user id from check method'


    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        auth_sid = self.response1.cookies.get('auth_sid')
        token = self.response1.headers.get('x-csrt-token')

        if condition == 'no_cookies':
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={'x-csrf-token': token}
            )
        else:
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={'auth_sid': auth_sid}
            )

        assert 'user_id' in response2.json(), \
            "there is no user id in second response"

        user_id_from_check_method = response2.json()['user_id']

        assert user_id_from_check_method == 0, \
            f'user is authorised with condition {condition}'