def decorator_function(original_function):
    def wrap_function():
        print("learn decorators")
        return original_function()
    return wrap_function


@decorator_function
def my_function():
    return "This is the original function."


result = my_function()
print(result)
