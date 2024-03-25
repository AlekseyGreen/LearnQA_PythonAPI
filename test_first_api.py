import requests

class TestFirstAPI:
    def test_hello_call(self):
        url = 'https://playground.learnqa.ru/api/helo'
        name = 'Aleksey'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, \
            "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_respons_text = response_dict['answer']
        assert expected_response_text == actual_respons_text, \
            'actual text  in response is not correct'
