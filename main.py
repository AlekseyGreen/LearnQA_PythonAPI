import requests

payload = {"name": "Aleksey"}
response = requests.get("https://playground.learnqa.ru/api/hello",
                        params=payload)
print(response.text)