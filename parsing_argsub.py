def decorat1(num):
    return num - 1

def decorat2(func):
    sub = 5
    return func(sub)


result = decorat2(decorat1)
print(result)
