def MyFunction(func):
    def wraps():
        print("Before function exected")
        func()
        print("After function executed")
    return wraps
@MyFunction
def Myfunction1():
    print("Welcome Ebi")
Myfunction1()