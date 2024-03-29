import pytest
import requests

class TestFirstAPI:
    # создаем переменную из которой будут последовательно браться значения
    names = [
        ('Vitalii'),
        ('Arseniy'),
        ('')
    ]
    @pytest.mark.parametrize('name', names) # указываем имя параметризированной переменной
    def test_hello_call(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, \
            "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = 'Hello, someone'
        else:
            expected_response_text = f"Hello, {name}"

        actual_respons_text = response_dict['answer']
        assert expected_response_text == actual_respons_text, \
            'actual text  in response is not correct'
