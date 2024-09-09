import json

data = {'name': 'Ebi', 'age': 22}
json_string = json.dumps(data)
print(json_string)

data_dict = json.loads(json_string)
print(data_dict)
