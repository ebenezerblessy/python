#Regular expression to validate a email address


import re
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = 'ebiebiangel@gmail.com'
if re.match(email_pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")