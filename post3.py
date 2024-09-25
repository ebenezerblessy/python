#storing in a variable

import requests
json_data = {'username':'Ebi','password':'1733'}
r = requests.post('https://httpbin.org/post',data = json_data)
r_dictionary= r.json()
print(r_dictionary['form'])