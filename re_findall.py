import re

pattern = "The rain in Spain gain"

matches = re.findall("ain", pattern)

print(matches)
