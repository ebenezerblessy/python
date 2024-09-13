def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function " + func.__name__)
        result = func(*args, **kwargs)
        print("Function " + func.__name__ + " finished")
        return result
    return wrapper

@log_decorator
def greet(name):
    print("Hello, {}!".format(name))

greet("Ebi")
