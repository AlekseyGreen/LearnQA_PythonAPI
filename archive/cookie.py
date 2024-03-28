import requests

url_get_cookie = "https://playground.learnqa.ru/api/get_auth_cookie"
url_check_cookie = "https://playground.learnqa.ru/api/check_auth_cookie"

payload = {"login": "secret_login", "password": "secret_pass"}
response_1 = requests.post(url_get_cookie, data=payload)

print(response_1.text)
print(response_1.status_code)
print(dict(response_1.cookies))
print(response_1.headers)
print()

cookie_value = response_1.cookies.get('auth_cookie')

cookies ={}
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})

response_2 = requests.post(url_check_cookie, cookies=cookies)
print(response_2.text)
print(response_2.status_code)
print(dict(response_2.cookies))
print(response_2.headers)
