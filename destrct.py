#Destrctors
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __del__(self):
        print("Welcome ebi")
person=Person("ebiangel", 22)
print(person.name)
print(person.age)