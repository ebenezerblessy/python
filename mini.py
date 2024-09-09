def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


number1 = int(input("Eneter a number"))
number2 = int(input("Eneter a number"))

lowest = minimum(number1, number2)
print("The lowest number between", number1, "and", number2, "is", lowest)

