import requests

response = requests.get('https://kitecareer.com/')
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
else:
    print('Error:', response.status_code)
