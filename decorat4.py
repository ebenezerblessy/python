def outer(a):
    def inner(b):
        return a / b
    return inner

div = outer(77)
res = div(7)
print(res)
