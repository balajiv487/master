class Dog:
    def __init__(self, name):
        self.name=name
d=Dog("Balaji")
print(d.name)

class Car:
    def __init__(self,name):
        self.name=name
class User:
    def __init__(self,name):
        self.name=name


class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    def speak(self):
        print("Bark")