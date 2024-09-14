import re
a = open("a.txt", "r")

b = a.read()
c = b.split("\n")
for d in c:
	obj = re.search(r'[\w.]+\@[\w.]+', d)
	if obj:
		print("Valid Email")
	else:
		print("Invalid Email")
