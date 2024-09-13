def main_decorator(func):
    def inner1():
        print("before first inner function executed")
        print("after first inner function executed")
        func()
    def inner2():
        print("before second inner function executed")
        func()
        print("after second inner function executed")
    def inner3():
        print("before third inner function executed")
        print("after third inner function executed")
        func()
    def wrapper():
        inner1()
        inner2()
        inner3()

    return wrapper

@main_decorator
def sub_decor():
    print("Its my fifth decorator function")

sub_decor()
