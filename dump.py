import json

my_data = {
    "name": "ebi",
    "age": 23,
    "is_student": False,
    "courses": ["Math", "Biology"],
    "address": {
        "street": "123 Main St",
        "city": "tenkasi"
    }
}

json_string = json.dumps(my_data, indent=4, separators=(',', ': '))
print(json_string)
