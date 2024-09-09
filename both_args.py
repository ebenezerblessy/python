def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("Good", "morning", "Ebi")
myFun(*args)

kwargs = {"arg1": "Hello", "arg2": "ebi", "arg3": "Greatday"}
myFun(**kwargs)
