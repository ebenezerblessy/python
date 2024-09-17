print('''please Select the Operation you  want to Perfom
      1 = Add
      2 = Subtract
      3 = Multiply
      4 = Divide''')

opt = int(input("Choose Operation from 1, 2, 3, 4 = "))

n1 = int(input("Enter a First Number        = "))
n2 = int(input("Enter a Second Number = "))

if opt == 1:
    print(n1, ' + ', n2, '  =  ', n1 + n2)
elif opt == 2:
    print(n1, ' - ', n2, '  =  ', n1 - n2)
elif opt == 3:
    print(n1, ' * ', n2, '  =  ', n1 * n2)
elif opt == 4:
    print(n1, ' / ', n2, '  =  ', n1 / n2)
else:
    print('Invalid Input')