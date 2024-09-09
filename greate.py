def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


number1 = int(input("Eneter a number"))
number2 = int(input("Eneter a number"))

greatest = maximum(number1, number2)
print("The greatest number between", number1, "and", number2, "is", greatest)

