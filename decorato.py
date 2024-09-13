#Creating decorators

def up_decor(function):
    def wrap_func():
        func = function()
        make_upper = func.upper()
        return make_upper

    return wrap_func