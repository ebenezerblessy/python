import requests
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'Name': 'Ebi',
    'location': 'surandai',
    'position': 'Python Developer',
    'company': 'KiteCareer',
    'userId': 1
}
response = requests.post(url, json=data)
if response.status_code == 201:
    print('Post created successfully:', response.json())
else:
    print('Failed with status code:', response.status_code)
