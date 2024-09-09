
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)
def lcm(a, b):
    return abs(a * b) // hcf(a, b)


first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print('LCM of', first, 'and', second, 'is', lcm(first, second))
