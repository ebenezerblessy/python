def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("ebi")
print(greet())