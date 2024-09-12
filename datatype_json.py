import json

json_data = '''
{
  "name": "ebi",
  "age": 22,
  "isEmployee": false,
  "courses": ["python", "django", "API"],
  "address": {
    "street": "first St",
    "city": "tenkasi"
  },
  "Trainee": null
}
'''

data = json.loads(json_data)

print("Name (String):", data["name"])
print("Age (Number):", data["age"])
print("Is Employee (Boolean):", data["isEmployee"])
print("Courses (Array):", data["courses"])
print("Address (Object):", data["address"])
print("Trainee (Null):", data["Trainee"])

json_string = json.dumps(data, indent=4)
print("\nConverted JSON string:")
print(json_string)
