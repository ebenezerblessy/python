import re

pattern = r'\d+'
string = '173ebin'

match = re.match(pattern, string)
if match:
    print('Match found:', match.group())
else:
    print('No match')
