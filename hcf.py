def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print('HCF of', first, 'and', second, 'is', hcf(first, second))
