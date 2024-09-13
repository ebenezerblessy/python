from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """A simple function."""
    print("Hello!")

print(say_hello.__name__)
print(say_hello.__doc__) 
