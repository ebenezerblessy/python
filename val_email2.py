import re

regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def emailValid(email):
    if re.fullmatch(regex, email):
        print("The given email is valid")
    else:
        print("The given email is invalid")

emailValid("ebycse@gamil.com")
emailValid("ebiebiangel@gmail.com")
emailValid("e7@dm.we")
emailValid("@domain.us")
