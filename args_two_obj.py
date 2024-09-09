# **args using set values of object
class Car():

    def __init__(self, **kwargs):

        self.speed = kwargs['s']
        self.color = kwargs['c']

audi = Car(s=200, c='red')
bmw = Car(s=250, c='black')
mb = Car(s=190, c='white')

print(audi.color)
print(audi.speed)
print(bmw.color)
print(bmw.speed)
print(mb.color)
print(mb.speed)

