import requests

class TestExercise:

    def test_exercise_11(self):
        url_get_cookies = 'https://playground.learnqa.ru/api/homework_cookie'
        response = requests.get(url_get_cookies)
        expected_cookie_value = 'hw_value'
        actual_response_cookie_value = response.cookies.get('HomeWork')
        assert expected_cookie_value == actual_response_cookie_value, \
            f"Значение cookie не совпадает с {expected_cookie_value}"