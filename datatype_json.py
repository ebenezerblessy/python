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
  "Student": null
}
'''

data = json.loads(json_data)

print("Name (String):", data["name"])
print("Age (Number):", data["age"])
print("Is Employee (Boolean):", data["isEmployee"])
print("Courses (Array):", data["courses"])
print("Address (Object):", data["address"])
print("Student (Null):", data["Student"])

json_string = json.dumps(data, indent=4, separators=(".","="))
print("Converted JSON string:")
print(json_string)
