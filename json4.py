import json


json_data = '{"name": "ebi", "dept": "python", "location": "uthumalai"}'


data = json.loads(json_data)

print(data['name'], data['dept'], data['location'])


json_data = json.dumps(data)

print(json_data)
