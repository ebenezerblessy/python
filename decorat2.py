def my_decorator(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

@my_decorator
def my_decor():
    print("Hello Ebi")
my_decor()
