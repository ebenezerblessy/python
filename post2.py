#convert JSON to Python Dictionary
import requests

json_data = {'username': 'Ebi', 'password': '1733'}
r = requests.post('https://httpbin.org/post', data=json_data)

print(r.json())
