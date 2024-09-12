def outer(a):
    def inner(b):
        return a * b
    return inner

mult = outer(3)
res = mult(7)
print(res)
