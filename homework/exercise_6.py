import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

redirect_count = len(response.history)
final_url = response.url

print(f"Количество редиректов в запросе {redirect_count}, "
      f"итоговый URL {final_url}")