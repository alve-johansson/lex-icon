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