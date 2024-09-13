
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("a is the greatest")
elif b > a and b > c:
    print("b is the greatest")
elif c > a and c > b:
    print("c is the greatest")
else:
    print("There is no greatest number")
