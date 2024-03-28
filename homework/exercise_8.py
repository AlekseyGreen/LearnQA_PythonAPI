import json
import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)
obj = json.loads(response.text)
token = obj['token']
delay_time = obj['seconds']

payload = {"token": token}
response_2 = requests.get(url, params=payload)
obj_resp_2 = json.loads(response_2.text)
if obj_resp_2['status'] == 'Job is NOT ready':
    print(f"Не торопись, задача еще не готова. Поле status: {obj_resp_2['status']}")
else:
    print('Ошибка')


time.sleep(delay_time)
payload = {"token": token}
response_3 = requests.get(url, params=payload)
obj_resp_3 = json.loads(response_3.text)
if obj_resp_3['status'] == 'Job is ready' and 'result' in obj_resp_3:
    print(f"А ты терпелив! Задача готова. Поле status: {obj_resp_3['status']}, "
          f"result: {obj_resp_3['result']}")
else:
    print("Да что за....!?")

