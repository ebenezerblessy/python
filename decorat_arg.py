def add(a, b):
    return a + b

def calculate(func, a, b):
    return func(a, b)  

res = calculate(add, 3, 7)
print(res)
