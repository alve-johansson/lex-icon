#---------------------------------------------

#Problem

# class Course:
#     def __init__(self, name, student = []):
#         self.name = name
#         self.student = student



# class BadCourse:
#     def __init__(self, name, students = []):
#         self.name = name
#         self.students = students

#     def add_student(self, student):
#         self.students.append(student)


# course1 = BadCourse("Python")
# course2 = BadCourse("AI")

# course1.add_student("Ada")


# print(course1.students)
# print(course2.students)



# Correct pattern


# class Course:
#     def __init__(self, name, students = None):
#         self.name = name

#         if students is None:
#             students = []

#         self.students = students


#     def add_student(self, student):
#         self.students.append(student)


# course1 = Course("Python")
# course2 = Course("AI")

# course1.add_student("Ada")


# print(course1.students)
# print(course2.students)



#----------------------------------
# Dict VS Class


# Dict:

# student_dict = {
#     "name" : "Ada",
#     "score" : 91
# }


# # class:

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# student_object = Student("Ada", 91)




#------------------------------------------------------------------------------------------------------------------------

# OOP Part 2



# class Student:

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         if self.score >= 70:
#             return "PASS"

#         return "FAIL"


# student = Student("Ada", 91)

# print(student.name)
# print(student.score)
# print(student.get_status())


#--------------------------------------------------------------------

# Inheritance

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating.")


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating.")
    
        
# dog = Dog("Rex", 5)
# cat = Cat("Luna", 3)

# dog.eat()
# cat.eat()



# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating")


# class Dog(Animal):
#     pass


# class Cat(Animal):
#     pass


# dog = Dog("Rex", 5)
# cat = Cat("Luna", 3)


# print(dog.name)
# print(cat.name)


# dog.eat()
# cat.eat()


# Terminology


# Animal:

# parent class
# base class
# superclass


# Dog:

# child class 
# derived class
# subclass

# The "IS-A" test 



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"


# class Dog(Animal):
#     pass


# dog = Dog("Rex")

# print(dog.eat())
# print(dog.sleep())


#----------------------------------------------------

# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def eat(self):
#         return f"{self.name} is eating"




# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says woof!"


# dog = Dog("Rex")

# print(dog.eat())
# print(dog.bark())


# animal = Animal("Unknown")   

# print(animal.bark())         #  <--- NO NO!


#----------------------------------------------------

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

        
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed


# dog = Dog("Rex", 5, "Labrador")

# print(dog.name)
# print(dog.age)
# print(dog.breed)


# # super()

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#         self.is_alive = True

#         if age < 0:
#             raise ValueError("age cannot be negative!")

        
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name,age)

#         self.breed = breed


# # class Dog(Animal):
# #     def __init__(self, name, age, breed):
# #         self.name = name
# #         self.age = age
# #         self.is_alive = True

# #         if age < 0:
# #             raise ValueError("age cannot be negative!")
        
# #         self.breed = breed



# dog = Dog("Rex", 5, "Labrador")

# print(dog.name)
# print(dog.age)
# print(dog.breed)
# print(dog.is_alive)


#------------------------------------------------------------

# Method Overriding


# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return "Some animal sound"


# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"



# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"


# animal = Animal("Animal")
# dog = Dog("Rex")
# cat = Cat("Luna")

# print(animal.make_sound())
# print(dog.make_sound())
# print(cat.make_sound())




# class Employee:

#     def get_information(self):
#         return "Employee information"


# class Developer(Employee):

#     def get_information(self):
#         base_information = super().get_information()

#         return (base_information + "- Role: Developer")



# developer = Developer()

# print(developer.get_information())

#--------------------------------------------------------------------

# polymorphism


# class Dog:
#     def make_sound(self):
#         return "Woof!"


# class Cat:
#     def make_sound(self):
#         return "Meow!"



# class Cow:
#     def make_sound(self):
#         return "Moo!"


# animals = [
#     Dog(),
#     Cat(),
#     Cow()
# ]

# for animal in animals:
#     print(animal.make_sound())




#--------------------------------


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return "Unknown sound"


# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"


# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"





# animals = [
#     Dog("Rex"),
#     Cat("Luna"),
# ]

# for animal in animals:
#     print(
#         animal.name,
#         animal.make_sound()
# )



#--------------------------------
# Duck Typing

# class Robot:
#     def make_sound(self):
#         return "Beep!"


# class Dog:
#     def make_sound(self):
#         return "Woof!"


# things = [
#     Robot(),
#     Dog()
# ]


# for thing in things:
#     print(thing.make_sound())


#--------------------------------
# isinstance()


# class Animal:
#     pass

# class Dog(Animal):
#     pass

# dog = Dog()

# print(isinstance(dog,Dog))
# print(isinstance(dog,Animal))

# print(isinstance(dog, str))



# if isinstance(....):
# elif isinstance(....):
# elifif isinstance(....):



#--------------------------------
# __str__

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# student = Student("Ada", 91)

# print(student)




# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def __str__(self):
#         return f"{self.name} - Score: {self.score}"


# student = Student("Ada", 91)

# print(student)



# text = str(student)

# print(text)
# print(type(text))


#----------------------------------------

# __str__ with inheritance


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return(
#             f"{self.name} -"
#             f"Salary: {self.salary}"
#         )


# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)

#         self.language = language

#     def __str__(self):
#         return (
#             f"{self.name} - Developer -"
#             f"{self.language}"
#         )

# employee = Employee("Grace", 45000)

# developer = Developer("Ada", 55000, "Python")


# print(employee)
# print(developer)


#----------------------------------------


# IS-A (Inheritance)

# HAS-A (Composition)


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine


engine = Engine(200)

car = Car("Volvo", engine)


print(car.brand)
print(car.engine.horsepower)
