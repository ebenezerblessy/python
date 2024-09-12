import json


data1 = {
    "name": 'ebiangel',
    "dept": 'python',
    "location": 'uthumalai',
    "company": 'kite',
    "district": 'tenkasi'
}

str1 = json.dumps(data1)
print(str1)
