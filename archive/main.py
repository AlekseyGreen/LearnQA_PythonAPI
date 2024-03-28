import requests

response = requests.post("https://playground.learnqa.ru/api/check_type",
                         data= {'name': 'Aleskey'})

print(response.text)