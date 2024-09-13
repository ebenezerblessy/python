#static method & class method in decorators

class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print("This is a class method. cls:", cls)

MyClass.static_method()
MyClass.class_method()