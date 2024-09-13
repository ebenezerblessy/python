#Multilpe decorators in single function

import functools

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def split_decorator(func):
    @functools.wraps(func)
    def wrapper():
        result = func()
        return result.split()
    return wrapper


def reverse_decorator(func):
    @functools.wraps(func)
    def wrapper():
        result = func()

        return result[::-1]
    return wrapper


def original_function():
    return "welcome ebi"


@reverse_decorator
@split_decorator
@uppercase_decorator
def decorated_function():
    return original_function()


result = decorated_function()
print(result)
