# *args using set values of object
class Car():

    def __init__(self, *args):

        self.speed = args[0]
        self.color = args[1]



audi = Car(200, 'red')
bmw = Car(250, 'black')
mb = Car(190, 'white')


print(audi.color)
print(audi.speed)
print(bmw.color)
print(bmw.speed)
print(mb.color)
print(mb.speed)
