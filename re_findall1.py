import re

string = "hey ebi"

match = re.findall("ebin", string)
print(match)

if (match):
  print("Yes, there is at least one match!")
else:
  print("No match")