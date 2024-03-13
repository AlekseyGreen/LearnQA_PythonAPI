import json

string_as_json_format = '{"answer":"Hello, user"}'
obj = json.loads(string_as_json_format) #парсим строку и кладем ее в переменную obj как словарь
key = 'answer2'

if key in obj:
    print(obj['answer']) #печатаем значение по ключу 'answer'
else:
    print(f"Ключа {key} в json нет")