######################
# METHOD OVERWRITING #
######################


################
# POLYMORPHISM #
################
""" 
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "unknown sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

animals = [
    Dog("rex"),
    Cat("Luna"),
    Cow("Moa")
]

for animal in animals:
    print(animal.make_sound()) #same function same logic different result different objects
    print(animal.name) """

""" class Robot:
    def make_sound(self):
        return "BEEP!"

class Dog:
    def make_sound(self):
        return "Woof!"

things = [
    Robot(),
    Dog()
]

for thing in things:
    print(thing.make_sound()) """
""" 
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal)) """

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return(f"{self.name} - AmAZING ")


print(Employee.__str__("banana"))