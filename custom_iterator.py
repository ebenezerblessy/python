class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_num = Numbers()
my_iter = iter(my_num)

for number in my_iter:
    print(number)
