#class = definition/blueprint
#object instance of the class


class Student: #naming convention is BankAccountEtc
    pass

""" student1 = Student()
student2 = Student()

print(student1)
print(student2)

print(student1 is student2)
 """

""" student1 = Student()
student1.name = "Ada" #attributes
student1.score = 91

print(student1.name, student1.score)

student2 = Student()
student2.name = "Grace" #attributes
student2.score = 22

print(student2.name, student2.score)

student3 = Student()
student3.name = "Alan"

print(student3.score) """
#-------------------------------------------------------------------
# PARAMETERS VS ATTRIBUTES

""" class Student:
    def __init__(self, name, score):    # self is just a naming convention
        self.name = name                # USE IT. name and score are parameters
        self.score = score              # one could have written self.name = student_name if ya change the parameters
 """
#object state == the values assigned of the attributes inside the class

""" student1 = Student("Ada", 91)
print(student1.name)
 """
#---------------------------------------------------------------------
#  SELF REFERS TOO THE SPECIFIC OBJECT WE ARE CURRENTLY WORKING WITH:
#  IF WE ARE WORKING WITH STUDENT1, SELF IS STUDENT1
#  THE CLASS IS THE DEAD OBJECT. SELF IS THE LIVE OBJECT
#  SOUNDS LIKE SOME POSTHUMANIST MARXISM
#----------------------------------------------------------------------

""" student2 = Student("Emma", 99)
print(student2.name)
 """
#-----------------------------------------------------------------------

# DEFAULT VALUES

""" class Student:              
    def __init__(self, name, score = 0, active = True):
        self.name = name
        self.score = score
        self.active = active """

# CLASS METHOD OBJECT METHOD SOMETHING METHOD

"""  def introduce(self): 
        print("Hello my name is", self.name)

    def get_status(self):
        if self.score >= 70:
            return "pass"

        return "fail"

student1 = Student("Ada", 91)
student2 = Student("Bob", 52)

print(student1.name, student1.score, student1.active)
print(student2.name, student2.score, student2.active) """

# KEYWORD ARGUMENTS WORK
""" 
student3 = Student(
    name = "Grace", 
    active = False,
    score = 99
)

print(student3.name, student3.score, student3.active)
student1.introduce()

print(student1.get_status())
print(student2.get_status())
print(student3.get_status())
 """

############################################################
# VALIDATION
#################################

""" class Student:              
    def __init__(self, name, score = 0, active = True):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        if new_score < 0 and new_score > 100:
            raise ValueError(
                "Score must be between 0 and 100"
            )
        self.score = new_score
 """

# THIS METHOD CHANGES THE STATE OBJECT; THE STATE OF THE OBJECT.

""" student = Student("Ada", 80)
print(student.score)
student.update_score(95)
print(student.score) """

""" class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

account = BankAccount("Ada", 1000)

print(account.balance) """

""" class Student: """
    ### CLASS ATTRIBUTE ####
    ### BELONGS TO THE CLASS ITSELF ###
"""     school = "Lexicon"              
    def __init__(self, name, score = 0, active = True): """
        ### INSTANCE ATTRIBUTE ###
        ### BELONGS ONLY TO INSTANCE ###
"""         self.name = name

student1 = Student("Ada")
student2 = Student("Grace")
 """

### CHANGEING INSTANCE ATTRIBUTE: ###
""" student1.name = "Ada Lovelace"
student1.school = "bananan school"

Student.school = "AI Academy"
print(Student.school)
print(student1.school) """

##################################################
# CLASS ATTRIBUTES -> SHARED CLASSE-LEVEL DATA
# INSTANCE ATTRIBUTES ->  DATA BELONGING TO AN INDIVIDUAL OBJECT
##################################################
""" 
class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (1 + self.tax_rate)

product1 = Product("Keyboard", 800)
product2 = Product("Mouse", 300)

print(product1.price_with_tax(), product2.price_with_tax()) """



##########################
# COLLECTIONS OF OBJECTS #
##########################

""" class Student:              
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
    Student("Charlie", 91)
]

for student in students:
    print(
        student.name,
        student.score,
        student.get_status()
    ) """

######################
# LIST COMPREHENSION #
######################

""" 
passed_students = [
    student 
    for student in students
    if student.score >= 70
]

for student in passed_students:
    print(student.name) """

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