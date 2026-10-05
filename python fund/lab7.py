"""  LAB 7  """
## PART A
""" 
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("Das Kapital", "K. Marx", 1002)
book2 = Book("", "N. Weiner", 200)
book3 = Book("Soumission", "M. Houellebecq", 321)
book4 = Book("BIBLE", "JESUS GOD ET AL", 2301)

print(book4.title)
print(book3.pages)
print(book2.author)
print(book1.pages, book1.title)
 """
""" class Laptop:
    def __init__(self, brand, model, ram_gb, price = 200):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Lenovo", "Thinkpad", "16", 3000)
laptop2 = Laptop("Jollaphone", "it's a phone", "16", 3000)
laptop3 = Laptop("HP", "x360 edge", "16", 5000)
print(laptop1.price)

laptop1.price = 2000

print(laptop1.price)

laptop4 = Laptop("Lenovo", "Thinkpad", "16", 3000)
laptop5 = Laptop("Lenovo", "Thinkpad", "16", 3000)
laptop6 = Laptop(price = 2299, brand = "alienware", model = "Bananabread pudding", ram_gb=20)

print(laptop4 is laptop5)
print(laptop6.model)
 """
## PART B

""" class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self, pages):
        if self.pages > 300:
            return "LONG"
        return "SHORT"

book1 = Book("Das Kapital", "K. Marx", 1002)
print(book1.is_long(book1.pages))
 """
""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, added_balance):
        self.added_balance = added_balance
        self.balance = self.balance + added_balance

    def withdraw(self, withdraw_value):
            self.withdraw_value = withdraw_value
            if withdraw_value > self.balance:
                raise ValueError(
                "Score must be between 0 and 100"
            )
            self.balance = self.balance - withdraw_value

myaccount = BankAccount("Alve", 3000)

myaccount.withdraw(200)

print(myaccount.balance)

myaccount.deposit(400)

print(myaccount.balance)

myaccount.withdraw(3300) """

""" class Task:
    def __init__(self, title, completed = False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

task1 = Task("diska")
task2 = Task("svara mejl")

task2.complete()

print(task2.completed)

print(task1.completed)

task2.reopen()

print(task2.completed)

print(task1.completed) """

## PART C

""" class Product():
    tax_rate = 0.20

    def __init__(self, name, price, tax_rate = tax_rate):
        self.name = name
        self.price = price
        self.tax_rate = tax_rate

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

product1 = Product("banana", 10)
product2 = Product("apple", 8)
product3 = Product("avocado", 15, 0.25)

print(product1.price_with_tax())
print(product2.price_with_tax())
print(product3.price_with_tax())

print(product3.tax_rate)
print(product2.tax_rate)
print(Product.tax_rate) """

## PART D
""" 
class Student:              
    def __init__(self, name, score = 0, active = True):
        self.name = name
        self.score = score
        self.active = active 

    def introduce(self): 
        print("Hello my name is", self.name)

    def get_status(self):
        if self.score >= 70:
            return "PASS"
        return "FAIL"


students = [
    Student("Anna", 85),
    Student("Bob", 65),
    Student("Charlie", 91),
    Student("DAnna", 25),
    Student("EBob", 63),
    Student("FCharlie", 71)
]

for student in students:
    print(
        student.name,
        student.score,
        student.get_status()
    )

students_who_passed = [
    student.name
    for student in students
    if student.score > 70
]

print(students_who_passed) """

## PART E

""" class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name



teacher = Teacher("Grace")

course = Course(
    "Python Foundation",
    teacher
    )

student1 = Student("Ada")
student2 = Student("Grace")

course.add_student(student1)
course.add_student(student2)

for student in course.students:
    print(student.name)

print(course.teacher.name) """

## PART F

""" class Student:
    passing_score = 70
    def __init__(self, name, score):

        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        self.name = name
        self.score = score

    def get_status(self):
        return "PASS" if self.score >= self.passing_score else "FAIL"

    def update_score(self, new_score):
        if not (0 <= new_score <= 100):
            raise ValueError("Score must be between 0 and 100")
        self.score = new_score


class Teacher:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name, teacher, students=None):
        self.name = name
        self.teacher = teacher

        self.students = students if students is not None else []

    def add_student(self, student):

        self.students.append(student)

    def get_student_count(self):
        return len(self.students)

    def get_passed_students(self):

        return [student for student in self.students if student.get_status() == "PASS"]

    def students_above_tresh(self, treshold):
        return [student for student in self.students if student.score > treshold]


teacher = Teacher("Haithem")

students_list = [
    Student("Anna", 85),
    Student("Bob", 65),
    Student("Charlie", 91),
    Student("DAnna", 25),
    Student("EBob", 63),
    Student("FCharlie", 71)
]


course1 = Course("Python Fundamentals", teacher, students_list)


new_student = Student("Gilles", 100)
course1.add_student(new_student)


print(f"Course: {course1.name}")
print(f"Teacher: {course1.teacher.name}")
print(f"Total students: {course1.get_student_count()}")

passed_names = [s.name for s in course1.get_passed_students()]
print(f"Passed students: {', '.join(passed_names)}")

students_who_score_above_tresh = course1.students_above_tresh(80)
for student in students_who_score_above_tresh:
    print(student.name)


course2_students = [
    Student("Gilles", 90),
    Student("Mark", 75)
]


teacher2 = Teacher("Aladdin")
course2 = Course("AI Fundamentals", teacher2, course2_students)

print("Antal i kurs 1:", course1.get_student_count())
print("Antal i kurs 2:", course2.get_student_count()) """