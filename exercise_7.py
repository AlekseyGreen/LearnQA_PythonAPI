import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

def test_method(url, method):
      payload = {"method": method}
      response = requests.request(method, url, params=payload)

      return response.text

# 1. без параметра method
response_1 = requests.delete(url)
print(f"http-запрос любого типа без параметра method: {response_1.text}")

# 2. не из списка, HEAD
response_2 = test_method(url, "HEAD")
print(f"http-запрос не из списка: {response_2}")

# 3. с правильным значением method
response_3 = test_method(url, "POST")
print(f"запрос с правильным значением method: {response_3}")

# 4. в цикле проверяем все возможные сочетания реальных типов запроса и значений параметра method
method_list = ['GET', 'POST', 'PUT', 'DELETE']
for method in method_list:
      for payload_method in method_list:
          payload = {"method": payload_method}
          if payload_method == "GET":
              response_4 = requests.request(method, url, params=payload)

          else:
              response_4 = requests.request(method, url, data=payload)
          print(f"Тип запроса: {method}, передаваемый method: {payload_method},"
                  f"ответ: {response_4.text}")