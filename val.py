import re
 
def check(s):
	pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
	if re.match(pat,s):
		print("Valid Email")
	else:
		print("Invalid Email")

if __name__ == '__main__':


	email = "ebi312@gmail.com"


	check(email)

	email = "my.ownsite@our-earth.org"
	check(email)

	email = "ebi@gmaail.com"
	check(email)
