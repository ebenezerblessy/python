import json

with open('D:\js1.json', 'r') as file:
    data = json.load(file)

print(data['name'], data['dept'], data['location'])

json_data = json.dumps(data, indent=4)

print(json_data)
