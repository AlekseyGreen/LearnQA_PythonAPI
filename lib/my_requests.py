import requests
from lib.logger import Logger
import allure
class MyRequests:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f'POST request to {url}'):
            return MyRequests._send(url, data, headers, cookies, 'POST')
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None,
             cookies: dict = None):
        with allure.step(f'GET request to {url}'):
            return MyRequests._send(url, data, headers, cookies, 'GET')
    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None,
             cookies: dict = None):
        with allure.step(f'PUT request to {url}'):
            return MyRequests._send(url, data, headers, cookies, 'PUT')
    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None,
             cookies: dict = None):
        with allure.step(f'DELETE request to {url}'):
            return MyRequests._send(url, data, headers, cookies, 'DELETE')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f'https://playground.learnqa.ru/api{url}'

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, method, data, headers, cookies)

        if method == 'GET':
            response = requests.get(url, params=data,
                                     headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.get(url, data=data,
                                     headers=headers, cookies=cookies)
        elif method == 'PUT':
            response = requests.get(url, params=data,
                                     headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.get(url, params=data,
                                     headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad http method '{method}' was received")

        Logger.add_response(response)

        return response
