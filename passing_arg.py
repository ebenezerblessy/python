def decorat1(num):
    return num + 1

def decorat2(func):
    add = 5
    return func(add)


result = decorat2(decorat1)
print(result)
