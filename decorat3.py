def person(func):
    def inner():
        print("I got decorator")
        func()
    return inner

@person
def develop():
    print("I am a developer")

develop()
