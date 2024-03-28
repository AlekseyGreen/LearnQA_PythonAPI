import requests

class TestHeaders:
    def test_exercise_12(self):
        url_get_headers = 'https://playground.learnqa.ru/api/homework_header'
        response = requests.get(url_get_headers)
        actual_response = response.headers
        print(actual_response)

        expected_secret_header_value = 'Some secret value'

        actual_secret_header_value = actual_response.get('x-secret-homework-header')
        assert expected_secret_header_value == actual_secret_header_value, \
            f"Значение headers не совпадает с {expected_secret_header_value}"
