import re
pattern = r"\s"

string = "The rain in Spain"

search = re.search(pattern, string)

if search:
    print("The first white-space character is located in position:", search.start())
else:
    print("No white-space character found.")
