""" class EmailNotification:
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message

    def send(self):
        return f"you Got an EMAIL {self.timestamp}: {self.message}"

class SMSNotification:
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message

    def send(self):
        return f"you Got an SMALL MESSAGE SERVICE: {self.timestamp}: {self.message}"

class PushNotification:
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message

    def send(self):
        return f"you Got a PUSH {self.timestamp}: {self.message}"


email = EmailNotification(14.00, " HEJ SVARA PÅ MEJLET")
sms = SMSNotification(14.30, "HEJ JAG SKICKADE ETT MAEJL KAN DU SVARA")
push = PushNotification(14.45, "HEJ VAR ÄR DUUUUUUUUUUUUUUUUU ??!")

NOTIFICICATION = [email, sms, push]

for notice in NOTIFICICATION:
    print(notice.send()) """

######## PART B

""" class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return f"This document is called '{self.title}'"

class PDFDocument(Document):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages

    def describe(self):
        return f"{super().describe()} and is {self.pages} pages long."

class TextDocument(Document):
    def __init__(self, title, characters):
        super().__init__(title)
        self.characters = characters

    def describe(self):
        return f"{super().describe()} and is {self.characters} characters long."

text1 = PDFDocument("Das Kapital", 1000)
text2 = PDFDocument("GBG - en berättelse om en stad", 300)
text3 = TextDocument("lösenord.txt", 524)
text4 = TextDocument("att göra listan.txt", 534)

texter = [text1, text2, text3, text4]

for text in texter:
    print(text.describe())
 """

##### PART C
""" 
class Printer:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def display_status(self):
        return f"this is a Printer from {self.brand} and it's {self.cost} quid"


class Screen:
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

    def display_status(self):
        return f"this is a Screen from {self.brand} and it's {self.cost} quid"

list1 = [
        screen1 := Screen("Msi", 200),
        screen2 := Screen("TUF gaming", 230),
        printer1 := Printer("Dell", 100),
        printer2 := Printer("Brother", 150)
        ]

for item in list1:
    print(item.display_status()) """
## ITS SAME NAME FUNCTION :D

################# PART D
""" class User:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

class AdminUser(User):
    def __init__(self, username, adress):
        super().__init__(username, adress)

obj = AdminUser("ALve", "Beväringsgatan 19")

print(isinstance(obj, User))
print(isinstance(obj, AdminUser))
print(isinstance(obj, str)) """
# ITS CHILDREN OF PATERN :)

############## PART E
""" class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        self.name = self.name.upper()
        return (
            f"Lemme hear you say this shit is {self.name}S\n"
            f"{" - ".join(self.name) + " - S "} \n"
            f"This shit is {self.name}S\n"
            f"{" - ".join(self.name) + " - S "} \n"
            f"Again, this shit is {self.name}S\n"
            f"{" - ".join(self.name) + " - S "} \n"
            f"This shit is {self.name}S\n"
            f"{" - ".join(self.name) + " - S "} \n"
        )
banana = Product("Banana", 10)
lemon = Product("Lemon", 10)
orange = Product("Orange", 10)

print(banana)
print(lemon)
print(orange)

x = str(banana)
print(type(x)) """

########### PART F
""" class Account:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"OWBED BY: {self.owner} MONEY: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
         super().__init__(owner, balance)
         self.rate = rate

    def __str__(self):
        return Account.__str__(self) + f"RATE: {self.rate}"

savies = SavingsAccount("Alve", 70000, 0.06)
monies = Account("ALVE", 123)
print(savies)
print(monies) """

############# PART G_G_G_G_G
#class CPU:
#    def __init__(self, model):
#        self.model = model
#
#class Computer:
#    def __init__(self, brand, CPU):
#        self.brand = brand
#        self.CPU = CPU
#
#
#cpu = CPU("Ryzen 7U")
#computer = Computer("Thinkpad", cpu)
#
#print(computer.brand, computer.CPU.model)
#
#print(hasattr(computer, "CPU"))
#
#Computer in fact has CPU and is not a CPU since they don't share attributes.


class Exporter:
    def __init__(self, data):
        self.data = data

    def export(self):
        return f"this is the {self.data}"

    def __str__(self):
        return f"cool bananas {self.data} style"

class ConsoleExporter(Exporter):
    def __init__(self, data, numb):
        super().__init__(data)
        self.numb = numb

    def export(self):
        return Exporter.export(self) + f" mit the number {self.numb}"

    def __str__(self):
        return f"cool bananas {self.numb} style"

class TextExporter(Exporter):
    def __init__(self, data, char):
        super().__init__(data)
        self.char = char

    def export(self):
        return Exporter.export(self) + f" mit the word {self.char}"

    def __str__(self):
        return f"cool bananas {self.char} style"

class SummaryExporter(Exporter):
    def __init__(self, data, floa):
        super().__init__(data)
        self.floa = floa

    def export(self):
        return Exporter.export(self) + f" mit the number {self.floa}"

    def __str__(self):
        return f"cool bananas {self.floa} style"

lista = [
    obj1 := SummaryExporter("school", 2.8),
    obj2 := TextExporter("schooliocoolio", "cool"),
    obj3 := ConsoleExporter("scolios", 123),
    obj4 := Exporter("wagamama")
]

for obj in lista:
    print(obj)

print(isinstance(obj1, Exporter))
print(isinstance(obj2, ConsoleExporter))
print(isinstance(obj3, Exporter))
print(isinstance(obj4, TextExporter))

print(hasattr(obj1, "floa"))
