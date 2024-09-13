print("Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("Enter choice (1-4): ")


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
    print("Invalid input. Please enter numeric values.")
else:
    num1 = float(num1)
    num2 = float(num2)


    if choice == '1':
        result = num1 + num2
        print(num1, "+", num2, "=", result)

    elif choice == '2':
        result = num1 - num2
        print(num1, "-", num2, "=", result)

    elif choice == '3':
        result = num1 * num2
        print(num1, "*", num2, "=", result)

    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            result = num1 / num2
            print(num1, "/", num2, "=", result)

    else:
        print("Invalid choice. Please select a number between 1 and 4.")
