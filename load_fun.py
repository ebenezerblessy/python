import json

x = '{"name": "ebi", "dept": "python", "location": "Uthumalai"}'

y = json.loads(x)

print(y["dept"])
