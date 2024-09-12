import json


data3 = {
    "name": 'ebi',
    "dept": 'python',
    "location": 'uthumalai'
}
c = json.dumps(data3)
print(c)
print(type(c))

b = json.loads(c)
print(b)
print(b["name"])

