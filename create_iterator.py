class MyNumber:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        y = self.a
        self.a += 1
        return y


my_class = MyNumber()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


