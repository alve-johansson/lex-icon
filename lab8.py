""" class BadTeam:
    def __init__(self, name, members = []):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.member = member
        self.members.append(member)


bb_members = []

team_a = BadTeam("bad boyz")

team_b = BadTeam("good boys")

team_a.add_member("Kenny")
team_a.add_member("Spenny")
team_a.add_member("Denny")
team_b.add_member("Spendrys")
print(team_a.members)             ############
                                  ### BAD ####
for member in team_a.members:     ############
    print(member)

print(team_b.members) """

""" class Team:
    def __init__(self, name, members = None):
        self.name = name
        self.members = members if members is not None else []

    def add_member(self, member):
        self.member = member
        self.members.append(member)


bb_members = []

team_a = Team("bad boyz")

team_b = Team("good boys")

team_a.add_member("Kenny")
team_a.add_member("Spenny")
team_a.add_member("Denny")
team_b.add_member("Spendrys")
print(team_a.members)             ############
                                  ### GOOD ###
for member in team_a.members:     ############
    print(member)

print(team_b.members)

 """

############### PART B ########################

""" movie = {"title": "titanic", "director" : "James Cameron", "Score" : 8.0}

class Movie:
    def __init__(self, title, director, score):
        self.title = title
        self.director = director
        self.score = score

    def good_score_questionmark(self):
        if self.score > 7.3:
            return f"ITS A HIGH SCORE"
        return f"ITS NOT A HIGH SCORE"


titanic = Movie("titanic", "james cameron", 8.0)

print(titanic.good_score_questionmark())
 """

#PART C

""" class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
     def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

monies = Account("Alve", 0)
savies = SavingsAccount("Alve", 70000, 0.2)

print(savies.balance)
print(isinstance(monies, Account)) 
print(isinstance(monies, SavingsAccount)) 
print(isinstance(savies, Account)) 
print(isinstance(savies, SavingsAccount))  """

### PART D
""" 
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information():
        pass

class Developer(Employee):
    def __init__(self, name, salary):
            super().__init__(name)

    def develope(self):
        print(f"{self.name} b developin'")

class Cleaner(Employee):
    def __init__(self, name, salary):
            super().__init__(name)

    def clean(self):
        print(f"{self.name} b cleanin'")


alve = Employee("Alve")
#alve.develope() #ERROR

alve2 = Developer("Alve", 999999999)
alve2.develope()

alve3 = Cleaner("Alve", 15000)
alve3.clean()
#alve3.develope() # ERROR

print(issubclass(Cleaner, Employee))
print(issubclass(Cleaner, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Employee, Cleaner))
 """
### PART E
""" class Device:
    def __init__(self, brand, year, active = True):
        self.brand = brand
        self.year = year
        if (2000 <= self.year <= 2026):
            self.year = year
        else:
            raise ValueError("Must be bought between year 2000 and 2026, older than that is pretty much GRave")
        
        self.active = True

class Laptop(Device):
    def __init__(self, brand, year, active, ram_gb):
        super().__init__(brand, year, active)
        self.ram_gb = ram_gb

class Phone(Device):
    def __init__(self, brand, year, active, number):
        super().__init__(brand, year, active)
        self.number = number


one_plus = Phone("oneplus", 2021, True, "0736846359")
work_thinkpad = Laptop("Lenovo", 2026, True, 16)

print(one_plus.year)
print(work_thinkpad.brand) """

### PART G
class Report:
    def __init__(self):
        pass

    def get_summary(self):
        pass

class SalesReport(Report):
    def __init__(self):
        super() 