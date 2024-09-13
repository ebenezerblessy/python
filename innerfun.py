def f1(func):
    sub_in = 'Welcome'
    func()
    def f2():
        sub_in = 'ebi'
        print(sub_in)

    f2()
    print(sub_in)


def my_func():
    print("This is the function passed to f1.")
f1(my_func)
