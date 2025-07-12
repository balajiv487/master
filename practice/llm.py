class Vehicle:
    def general_usage(self):
        print("General use is : Transportation")
class Car(Vehicle):
    def __init__(self):
        print("I am a car")
        self.wheels=4
        self.has_roof=True

    def special_usage(self):
         print("Special use is : commute for work")

class Motorcycle(Vehicle):
    def __init__(self):
        print("I am a motorcycle")
        self.has_roof=False
        self.wheels=2
    def special_usage(self):
        print("Special use is : commute for work")
c=Car()
c.general_usage()
c.special_usage()

m=Motorcycle()
m.general_usage()
m.special_usage()