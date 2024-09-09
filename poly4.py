class Animal():
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dogs sound")
class Bird():
    def sound(self):
        print("Birds makes sound")
class Dove(Bird):
    def sound(self):
        print("dove sounds")
d1=Dog()
d1.sound()
b1=Bird()
b1.sound()
