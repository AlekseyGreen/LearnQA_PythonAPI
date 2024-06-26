from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name,
                                  expected_value, error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, \
                f"Response is not JSON format. Response text if '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        assert response_as_dict[name] == expected_value, error_massage

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, \
                f"Response is not JSON format. Response text if '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, \
                f"Response is not JSON format. Response text if '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key {name}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, \
                f"Response is not JSON format. Response text if '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}' . But its present"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            (f"Unexpected response status code! Expected: {expected_status_code}."
             f"Actual: {response.status_code}")