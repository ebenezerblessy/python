
def add():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return "Addition:", num1 + num2


def sub():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return "Subtraction:", num1 - num2

def mult():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return "Multiplication:", num1 * num2

def div():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return "Division:", num1 / num2

addition_result = add()
subtraction_result = sub()
multiplication_result = mult()
division_result = div()

print(addition_result)
print(subtraction_result)
print(multiplication_result)
print(division_result)