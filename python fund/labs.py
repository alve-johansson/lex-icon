#print("alve")
#print("lexucoin")
#print("python fundamentals")
#p_name, p_age, p_height = "alve", 32, 1.83
#print(p_name, p_age, p_height)
#print(type(p_name)) #etc
#string_ten = "10"
#string_ten = int(string_ten)
#print(type(string_ten))
#x, y = 10, 5
#print(x + y, x-y, x**y, x//y)

#string to int = taking user input for mahts
#int to float = when math is 
#name = input()
#birthyear = int(input())
#year = 2026
#age = year - birthyear
#print(age)
#price = float(input())
#discount = float(input())
#discount = discount/100
#discount = 1-discount
#print(price*discount)
#temp_c = float(input())
#temp_f = temp_c*(9/5)+32
#print(temp_f)
#room_width = float(input())
#room_length = float(input())
#print(room_length*room_width)
#sentence = "hej jag Heter Alve"
#print(len(sentence), sentence.upper(), sentence.lower(), sentence.capitalize())
#print(sentence[::-1], sentence[0:7], sentence[-11:])
#name = input()
#surname = input()
#print(f"hej {name} {surname}!")
#txt = "python programming"
#print(txt[0], txt[-1],txt[:7], txt[-11:])
#email = "alvejohansson@pm.me"
#email = email.split("@")
#print(email)
#sentence = "bananer i java"
#sentence = sentence.replace("java", "python")
#print(sentence)
#txt = "hej jag heter alve"
#print(txt[1], txt[4:5], txt[::-1], txt[-3:-1], txt[::3], txt[1::2], txt[-1::2])
#txt = "artificial intelligence"
#print(txt[0:4], txt[::-1], txt[4:10], txt[11:16], txt[::2])
#txt = "                               bananer i pjyamas. hej jag heter alve. alvejohansson@pm.me"
#print(txt.strip(), txt.split("@"), txt.replace(" ", "-"))
#txt = "alve"

#txt2 = "o" + txt[1:]

#print(txt2)
#name = input()
#surname = input()
##city = input()
#birthyear = input()
#fav_lang = input()
#name.strip()
#surname.strip()
#city.strip()
##birthyear.strip()
#fav_lang.strip()
#user_id = name[0:3] + surname[0:3] + str(birthyear)
#print(user_id)
#print(f"hej testar {name[0:3]}, testar {fav_lang[::-1]}")x/10)
#minutes = input()
#minutes = int(minutes)
#hours = minutes // 60
#minutes_remaining = minutes % 60
#print("hours:", hours, "minutes:", minutes_remaining)
#x = 5669
#print(x % 10, (x//10)%10, (x//100)%10, (x//1000)%10)
#txt = "alvejohansson@gmail.com"
#stars = len(txt)-4
#print(txt[:2], "*"*stars, txt[-2:])
#lang = ["Python", "C#", "Go", "Rust", "C++", "Java"]
#print(lang[0], lang[-1], lang[2])
#print(lang[::-1], lang[::2])
#lang.append("Javascript")
#print(lang)
#lang.insert(2, "Perl")
#print(lang)
#lang2 = lang.pop(0)
#print(lang, lang2)
#lang.remove("Go")
#print(lang)

#nums = [1, 2, 8, 3, 4, 5, 6, 7]
#print(max(nums), min(nums), sum(nums))
#print(sorted(nums))
#print(nums)
#nums.sort()  #sort changes for good and sorted temporarily changes
#print(nums[::-1])

#nums2 = nums
#nums3 = nums.copy()
#nums[0] = 99999
#print(nums2, nums, nums3)

#rgb_values = ((1,2,3),(3,2,1),(4,5,6))
#rgb1 = rgb_values[0]
#print(rgb1[2])
#p1 = ("anna", 32, "gbg")
#print(f"hej {p1[0]}, har du fyllt {p1[1]} än? kvar i {p1[2]} fortfarande?")
 
#coordinates = ((10,20),(20,30),(30,40),(40,50))
#print(coordinates[0][1], coordinates[3][1])

#y = ["hello", "hello", "banana", "alve"]
#y = set(y)
#print(y)

#y = {"python", "c++", "perl", "javascript"}
#x = {"python", "java", "c#", "javascript"}
#print(y & x, y | x, y - x)
#y = {1, 2, 3, 4}
#y.add(5)
#print(y)
#y.discard(5)
#print(y)
#print(2 in y, 8 in y)
#laptop = {"brand": "asus", "model": "thinkpad t14", "ram_gb": 4, "storage_gb": 256, "price_usd": 250}
##print(laptop["brand"])
##laptop["price_usd"] = 150
##laptop["operating_system"] = "arch linux"
##print(laptop.pop("brand", None))
##print(laptop.pop("Banana", None))
##x = laptop.get("operating_system")
##print(x)
#print(laptop)
#books = [
#    {"title" : "lolita", "author" : "vladimir nabokov", "pages" : 420},
#    {"title" : "odysses", "author" : "homer", "pages" : 1337},
#    {"title" : "frankenstein", "author" : "marry shelly", "pages" : 69},
#    {"title" : "american psycho", "author" : "bret easton ellis", "pages" : 1466},
#    {"title" : "the holy bible", "author" : "g-sus christ", "pages" : 1234}
#             ]
#
#print(books[2]["title"])
#books[3]["status"] = "sold"
#
#print(books[3])
#cat = [
#    {"title" : "the big lebowski", "year" : 2002, "rating" : 8.3},
#    {"title" : "itanic", "year" : 2003, "rating" : 8.3},
#    {"title" : "the matrix", "year" : 1999, "rating" : 8.3},
#    {"title" : "marvel movie 56", "year" : 2026, "rating" : 8.3},
#    {"title" : "the room", "year" : 2009, "rating" : 9.9} 
#    ]
#
#print(cat[3]["rating"])
#print(f"min favoritfilm är {cat[4]["title"]}")
#title" : "the holy bible", "author" : "g-sus christ", "pages" : 1234}
#usernames_1 = ["albin", "sventro", "jord", "bajenpundare", "aik-trubaduren", "lifestalker"]
#usernames_2 = ["albin12", "sventro", "jordmåne", "bajenpundare", "aik-trubadure33n", "lifestalker"]
#
#usernames_3 = usernames_2 + usernames_1
#
#print(set(usernames_3))
#x = int(input())
#if x > 0:
#    print("positive")
#elif x == 0:
#    print("zero")
#else:
#    print("negative")
#x = int(input())
#if x > 65:
#    print("pensionär")
#elif x > 40:
#    print("medelålders?")
#elif x > 18:
#    print("vuxen")
#elif x > 15:
#    print("byxmyndig å moppe å sånt")
#else:
#    print("barn")
#usr = ""
#pw = ""
#print("give username:")
#usr = input()
#print("give password:")
#pw = input()
#
#real_usr = "admin"
#real_pw = "1111"
#
#if usr == real_usr and pw == real_pw:
#    print("logging in....")
#else:
#    print("try again...")
#grade = int(input())
#if grade > 90:
#    print("Nice")
#elif grade > 70:
#    print("decent")
#elif grade > 50:
#    print("ok")
#elif grade > 30:
#    print("not very good")
#else: 
#    print("kill yourself")
#shipping_cost = 20
#order_cost = int(input())
#member = True
#
#if order_cost > 100 and member == True:
#    shipping_cost = 0
#    print("total cost", shipping_cost + order_cost)
#else:
#    print("total cost", shipping_cost + order_cost)
#if True > False:
#    print("True is bigger than False")
#
#if True is bool:
#    print("True is bool")
#print("True is not bool?")
#
#if True is int or True > 0:
#    print("True is either int or more than 0")
#
#if True is not False:
#    print("True is not false, is not false True?")
#
#if not False is not (not True):
##    print("not false is not not true?")
#txt = ""
#txt2 = "x"
#num = 0
#numtxt = "0"
#listy = []
#listx = [0,0]
#
#if txt > txt2 and numtxt > num:
#    print("bananer i pyjamas")
#
#if listy > listx:
#    print("bananer i klänning")
#
#if txt == num:
#    print("skoj")
#
#if txt in listy or txt in listx:
#    print("123")
#
#for element in listx:
#    print(listx[0])
#
#lang = input()
#languages = ["python", "bananer","spaceghostpurple"]
#if lang in languages:
#    print(lang, "is in", languages)
#if lang not in languages:
#    print(lang, "is not in", languages)
#usr = input()
#blocked_usrs = ["alve", "ADMlN", "droak"]
#if usr in blocked_usrs:
#    print("BANNAD")

#usrs = ["alve", "ADMlN", "droak"]
#for usr in usrs:
#    print("Välkommen", usr)
#tot = 0
#
#for i in range(50):
#    if i % 2 == 0:
#        print(i)
#        tot += i
#
#print(tot)

#max = 0
#listy = [1,2,3,8,12,13,66,23,8]
#
#for num in listy:
#    if num > max:
#        max = num
#
#print(max)
#srs = ["alve", "ADMlN", "droak", "python", "bananer","spaceghostpurple"]
#tot = 0
#for word in srs:
#    if len(word) > 5:
#        tot += 1
#
#print(tot)

#listy = [1,2,3,8,12,13,66,23,8]
#passes = 0
#fails = 0
#for grade in listy:
#    if grade > 5:
#        passes += 1
#    else:
#        fails += 1
#
#print("passes", passes, fails, "fails")

#cat = {
#    "movie1" : {"title" : "the big lebowski", "year" : 2002, "rating" : 8.3},
#    "movie2" : {"title" : "itanic", "year" : 2003, "rating" : 8.3},
#    "movie3" : {"title" : "the matrix", "year" : 1999, "rating" : 8.3},
#    "movie4" : {"title" : "marvel movie 56", "year" : 2026, "rating" : 8.3},
#    "movie5" : {"title" : "the room", "year" : 2009, "rating" : 9.9} 
#    }
#
#for key in cat.keys():
#    print(key, cat[key]["title"], "is in my movie list")
#
#for release_date in cat.values():
#    print(release_date["year"])
#
#for key, movie_info in cat.items():
#    print(f"swag: {key}, {movie_info["rating"]}")

#for i in range(10, 0, -1):
#    print(i)

#x = int(input())
#for i in range(10):
#    print(str(x), "*", i, "=", x*i)

#srs = ["alve", "ADMlN", "droak", "python", "bananer","spaceghostpurple"]
#
#for i, usr in enumerate(srs, 1):
#    for y, usr in enumerate(srs, 1):
#        print(i, y, usr)
#x = 10
#
#while x >= 0:
#    print(x)
#    x -= 1
#
#x = ""
#y = "pass123"
#while x != y:
#    print("skriv ditt lösenord")
#    x = input()
#print("rätt lösenord")
#
#menu = 0
#while menu != 4:
#    print("vad vill du göra" \
#    "1. inställningar" \
#    "2. spela" \
#    "3. lägga till kompis" \
#    "4. stänga av")
#    menu = int(input())
#x = 12333
#y = 0
#
#while x != 0:
#    print("skriv ett tal")
#    x = int(input())
#    y +=1
#
#print(y)

#secret_number = 66
#guess = 0
#while guess != secret_number:
#    print("gissa det hemliga numret")
#    guess = int(input())
#    if guess > secret_number:
#        print("du gissade för högt")
#    elif guess < secret_number:
#        print("du gissade för lågt")
#print("rätt!")

#for i in range(1, 100, 1):
#    if i % 7 == 0 and i % 9 == 0:
#        print(i)
#        break
#
#listx = ["asd", "", "", "asd", "123", "123"," ", "", "123"]
#
#for string in listx:
#    if string == "":
#        continue
#    else:
#        print(string)
#srs = ["alve", "ADMlN", "droak", "python", "bananer","spaceghostpurple"]
#
#for name in srs:
#    if name == "droak":
#        print("found")
#        break
#srs = [1, 2, 3, 4, -1, -2, 2, -4, 5, 999, 123, 3234, 433, 999, 234]
#
#for num in srs:
#    if num < 0:
#        continue
#    elif num == 999:
#        break
#    else:
#        print(num)
#for i in range (1, 100, 1):
#    if i % 3 == 0 and i % 5 == 0:
#        print(i, "FizzBuzz")
#    elif i % 3 == 0:
#        print(i, "Fizz")
#    elif i % 5 == 0:
#        print(i, "Buzz")
#
#sentence = "hej jag heter alve å är 12 år swaeg"
#wovels = "aoueiyåäö"
#w_counter = 0
#
#for letter in sentence:
#    if letter in wovels:
#        w_counter += 1
#
#print(w_counter)

#listx = [1, 2, 3, 4, 5, 1, 2, 3, 1, -99, 123, 1, 2, 99]
#
#for i, num in enumerate(listx):
##    if num in listx[:i] or num in listx[i+1:]:
##        print(num," has dopio")
##    else:
##        print(num, "has nondopio")
#
#listx = [1, 2, 6, 4, 5, 6, 2, 1, 2, 6, 3, 1, 6, 6, 2, 4, 1, 2, 9]
#
#for i in range (10,0,-1):
#    for num in listx:
#        if num >= i:
#            print("** ", end = "")
#        else:
#            print("   ", end = "")
#    print(" ")
#print(listx)
#
#import time
#import random
#
## Simulerar en oändlig dataström (t.ex. CPU-användning eller sensor)
#while True:
#    # Generera ett värde mellan 1 och 10
#    datapunkt = random.randint(1, 10) 
#    
#    # Skapa stapeln direkt baserat på värdet
#    stapel = "*" * datapunkt
#    mellanrum = " " * (10 - datapunkt)
#    
#    # Skriv ut direkt (från vänster till höger)
#    print(f"{datapunkt:2d} | {stapel}{mellanrum} |")
#    
#    time.sleep(0.2) # Paus för att simulera realtid
#

#def greet(name, age): #name, age = parameter
#    return print("hello", name, ", your age is:", age)
#
#greet("Alve", 32) #alve, 32 = argument

""" '''LAB 4'''

def greet():
    return True
def show_course_name():
    return "banana"
def print_seperator():
    print(" ")

print(greet())
print_seperator()
print(show_course_name())
print(greet())
print_seperator()
print(show_course_name()) """

#shift + alt + a

""" def greet_person(name):
    print("Hello", name)

def introduce(name, city):
    print("Welcome to", city, ",", name, "!")

greet_person("Alve")
introduce("Alve", "Göteborg")
 """

""" def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b): #parameters in the function
    return a / b

a, b = 3, 5

print(add(a,b), subtract(a,b), multiply(a,b), divide(a,b)) #argument sent into the function """

""" def calculate_area(width, length):
    return width * length

def calculate_volume(area, height):
    return area * height

x = 230
y = 210
z = 0.1

print(calculate_volume(calculate_area(x, y), z))
 """

""" def is_even(num):
    return num % 2 == 0

print(is_even(234234)) """

""" def get_larger(a, b):
    if a >= b:
        return a
    else:
        return b

print(get_larger(13,11))
print(get_larger(11,14))
print(get_larger(12,12)) """

""" def classify_score(score):
    if score > 70:
        return "PASS"

    return "FAIL"

print(classify_score(123))
print(classify_score(12)) """

""" def greet(name, greeting = "Hello "):
    return(greeting + name)

print(greet("Alve"))
print(greet("Alve", "Konnichiwa "))
print(greet(greeting = "Alve", name = "Konnichiwa ")) """

""" def calculate_price(price, quantity = 1, discount = 0):
    return price * quantity * (100-discount)/100


print(calculate_price(100, 1, 30)) """

""" def create_profile(name, city = "unknown", active = True):
    return {"Name" : name, "City" : city, "Active" : active}

print(create_profile("Alve", "Göteborg")) """

""" def test(a, b):
    return b, a

print(test(b = 1, a = 2)) """
""" 
def calculate_total_even(nums):
    total_even = 0
    for num in nums:
        if num % 2 == 0:
            total_even += 1

    return total_even

listx = [1, 2, 3, 4, 5, 6, 7]

print(calculate_total_even(listx)) """

""" def get_long_words(words, minimum_length):
    listx = []

    for word in words:
        if len(word) > minimum_length:
            listx.append(word)

    return listx

listy = ["Hello", "dear", "this", "is", "the", "band", "'Have a nice life'", "playing", "as", "of", "right", "now"]

print(get_long_words(listy, 4)) """



""" def find_student(students, name):
    for student in students:  # Loopa igenom listan
        if student["student_name"] == name:
            return True
    return False


list_of_students = [
    {"student_name": "Alve"},
    {"student_name": "Damon"},
    {"student_name": "Per"},
    {"student_name": "stanley"},
    {"student_name": "benny"}
]

print(find_student(list_of_students, "Damon")) 
     """

""" def average_score(students):
    total = 0
    counter = 0
    for score in students:
        total += score
        counter += 1
        
    return total/counter

listx = [78,67,70,99,70,53,70,86,85]

print(average_score(listx)) """

""" def get_active_users(users):
    result = [user for user in users if user["active"]]
    return result

list_of_students = [
    {"student_name": "Alve", "active" : False},
    {"student_name": "Damon", "active" : True},
    {"student_name": "Per", "active" : True},
    {"student_name": "stanley", "active" : True},
    {"student_name": "benny", "active" : False}
]

print(get_active_users(list_of_students)) """

""" def c_to_f(c):
    return (c * 9/5) + 32

def classification(c):
    if c > 20:
        return "hot"
    elif c > 14:
        return "warm"
    else:
        return "cold"

def formatted_temp(c):
    fahrenheit = c_to_f(c)
    temp_class = classification(c)

    return f"The temperature is {c} celsius and {fahrenheit:.2f} fahrenheit, it's {temp_class}"

temps = [12, 18, 22, -5]

for temp in temps:
    print(formatted_temp(temp)) """

""" def subtotal(cost, quantity):

    return cost * quantity

def discount(discount):

    return (100-discount)/100

def final_total(subtotal, taxes, discount):

    return (subtotal * discount) * taxes

taxes = 1.30

price = 100
number_of_cakes = 4
discount_percentage = 25

s = subtotal(price, number_of_cakes)
d = discount(discount_percentage)

print(final_total(s, taxes, d)) """

""" Part F - Applied challenge: Event registration processor 
 
1. Create functions to normalize a participant name, validate an age range using boolean return values, calculate a registration fee based on age/student status, and create a participant dictionary. 
2. Create at least eight participant dictionaries using your functions. 
3. Write a function that receives the participant list and returns the total expected registration revenue. 
4. Write a function that returns only student participants. 
5. Write a function that returns the oldest participant. 
6. Write a function that creates a readable summary string for one participant. 
7. Keep input/output responsibilities separate from calculation functions as much as possible. """

""" def norm_name(name1, name2):
    return name1 + name2

def val_age_range(age):
    if age < 18 or age > 65:
        return True
    return False

def calc_fee(age, student):
    if student or val_age_range(age):
        return 50
    return 100



     """

""" "total = 100

def add_tax(total):
    total = total * 1.25
    return total

print(add_tax(total))" """


""" def return_minmax(listx):
    listx.sort()
    return listx[0], listx[-1]

lista = [1, 2, 3, 0, -999, 4, 999, 5, 6, 7]

print(return_minmax(lista)) """

""" def palindrome(word):
    x = len(word)//2
    for i in range(0, x-1, 1):
        if word[i] != word[-i]:
            print("ingen palle")
            return

    print("de e en palle")
    return True
        

print(palindrome(input())) """  

""" def palin(word):
    return word == word[::-1]

x = "anna"
print(palin(x)) """

""" def freq(text_input):
    freq_dict = {}
    for ltr in text_input:
        # Om 'ltr' inte finns än, ta 0 och plussa på 1.
        freq_dict[ltr] = freq_dict.get(ltr, 0) + 1
        
    return freq_dict

text = "hej jag heter alve bananer skoj bla bla bla"

print(freq(text)) """

""" def pz_or_n(nums):
    p, n, z, = 0, 0, 0

    for num in nums:
        if num > 0:
            p += 1
        elif num < 0:
            n += 1
        else:
            z += 1

    return {"positive" : p, "zero" : z, "negative" : n}


listx = [1, 2, 3, 4, 5, 0,0,0,0 , -1 ,-1 ,-2 ,-3 ,-4]

print(pz_or_n(listx))
 """

""" course_name = "lexicon"

def functionx():
    course_name = "bananer"
    print(course_name)
    return

functionx()

print(course_name) """
""" 
def counter123():
    counter = 0
    for i in range(0, 30, 1):
        counter += i

    print(counter)
    return


counter123()

print(counter) """

""" global_variable_x = 1

def change_global_fail():
    global_variable_x = 0
    return
G
change_global_fail()
print(global_variable_x)
 """

""" global_variable_x = 1

def change_global_fail(varx):
    varx = 0
    return varx

global_variable_x = change_global_fail(global_variable_x)
print(global_variable_x) """

""" def outer():
    x = 1
    def inner():
        print(x)
        return
    inner()
    return

outer() """

""" total_sum = 100
text_str = "Python"
numbers_list = [1, 2, 3]
max_value = 50 """

""" def add_all(*numbers):
    numsum = 0
    for num in numbers:
        numsum += num

    return numsum

nums = [1, 2, 3 ,3 ,4 ,5 ,6 ,7]

print(add_all(*nums)) """

""" def average(*nums):
    numsum = 0
    if len(nums) == 0:
        return f"no swagger"
    else:
        for num in nums:
            numsum += num

    return numsum/len(nums)

tal = []

print(average(*tal)) """
""" 
def longest_word(*words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word


    return longest


listx = ["alve", "palve", "paron", "pong", "asdasdsad", "asdasdölkasödlkasöldk"]

print(longest_word(*listx)) """

""" def build_sentence(separator, *words):
    newstring = separator.join(words)
    return newstring


x = build_sentence(" ---- ", "alve", "palve", "paron", "pong", "asdasdsad", "asdasdölkasödlkasöldk")
print(x) """

""" def describe_scores(student_name, *scores):
    number_of_scores = 0
    tot_score = 0
    for score in scores:
        number_of_scores += 1
        tot_score += score

    avg = tot_score/number_of_scores
    x = f"{student_name} has {number_of_scores} grades, with an average of {avg}"

    return x

print(describe_scores("Alve", 90, 89, 70, 74, 64, 66, 90)) """

""" tal = [10,20,30]

def add(a, b, c):
    return a + b + c

print(add(*tal)) """


""" mytuple = ("alve", "johansson", "gbg")


def funkychicken(*args):
    return f"fitta {args[0]} kuk {args[1]} gbg: {args[2]}"

print(funkychicken(*mytuple)) """

""" 
def add(first,*args, last):
    numsum = 0
    for arg, e in enumerate(args):
        numsum += arg[e]

    print(numsum)
    numsum += first
    numsum += last
    print(numsum)
    return numsum

lista = [1, 2, 2, 2, 2, 3]
listb = [1, 2, 2, 2,2,2,2,2, 2, 2, 3]
listc = [1, 2, 2, 2, 2, 3,3,3,3,3,3,3,3,3]

add(lista[0],lista[1:-2],last = lista[-1])
add(lista[0],lista[1:-2],last = lista[-1])
add(lista[0],lista[1:-2],last = lista[-1])
 """

""" values_1 = [10, 20, 30, 40, 50]
first, *middle, last = values_1

print(f"first: {first}")   
print(f"middle: {middle}")  
print(f"last: {last}")      

print("-" * 20)

values_2 = ["A", "B", "C"]
first, *middle, last = values_2

print(f"first: {first}")   
print(f"middle: {middle}")  
print(f"last: {last}")     

print("-" * 20)

values_3 = [1, 2]
first, *middle, last = values_3

print(f"first: {first}")   
print(f"middle: {middle}")  
print(f"last: {last}")      """

### difference, in function definition * means "unlimited"
#  parameters, but when calling a function in instead is a symbol or a function that unpacks a variable 

""" def show_profile(**info):
    for k,v, in info.items():
        print(k, v)

    return 

mydic = {"bananer" : "i pyjamas", "spagehetitit" : "gorgonzola", "123" : "abc"}

show_profile(**mydic) """
""" 
def create_user(username, **details):
    mydic = {username}
    for detail in details:
        mydic[username] = detail

    print(mydic)
    return """

""" numbers = [1, 2, 3, 4, 5]

doubled_numbers = [number * 2 for number in numbers]

print(doubled_numbers) """

""" numbers = [1,2,3]
square = [number ** 2 for number in numbers]
print(square) """

""" names = ["Alve", "Graham", "Harman"]
upper_names = [name.upper() for name in names]
print(upper_names) """

""" numbers = [1,2,3,4,5,6]
result = [number **2 for number in numbers if number % 2 == 0]
print(result) """

""" names = ["Ada", "Bob", "Alexander", "Grace", "Li"]

x = [name for name in names if len(name) >= 5]
print(x) """

""" 
numbers = [1,2,3,4,5] #keyz
squares = {number: number ** 2 for number in numbers}
print(squares) """

""" prices = {"apple" : 10, "banana" : 5, "orange" : 7}

d_prices = {product: price * 2 for product, price in prices.items()}
print(d_prices) """


""" for inex, lista in enumerate(lista):
    print(inex, lista) """
""" 

for index, lista in enumerate(lista, 5):
    print(index, lista) """

""" names = ["Anna", "Bob", "Charlie", "Darren"]
scores = [23, 42, 23]

student_scores = dict(zip(names, scores))

print(student_scores) """

""" numbers = [1, 2, 3, 4, 5, 6, 7]

first, *_, last = numbers

print(first)

print(last) """
""" 
first = [1, 2, 3]
second = [4, 5, 6]

combined = [*first, *second]

print(combined) """

""" double = lambda number: number * 2
print(double(5)) """

""" names = ["xaxxxxxxlve", "balve", "cae", "zalve"]

sorted_names = sorted(names, key=lambda name: len(name))

print(sorted_names) """

""" numbers = [ 1, 2 , 3 ,4 ,5 ,6 ,77]

doubled = map(lambda number: number * 2, numbers)
print(doubled)
print(*doubled) """


""" numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers) """