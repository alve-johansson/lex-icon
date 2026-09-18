### LAB 6
# PART A

""" squares = []

for i in range (1, 21, 1):
    squares.append(i**2)

print(squares)

squares = [x ** 2 for x in range(1, 21, 1)]
print(squares) """

""" even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers) """

""" names = ["Alve", "               cassandra", "heithem", "Gilles", "thomas"]

capital_names = [name.strip().capitalize() for name in names]

print(capital_names)     """

""" scores = [4, 20, 69, 1312, 420, 1337]
passing_scores = [score for score in scores if score > 400]
print(passing_scores)

labels = ["PASS" if score >= 400 else "FAIL" for score in scores]
print(labels) """

#skippar 6 och freestylar lite
""" 
c = [10, 25, 30, 35, -10, 0]

f = [(9/5)*x+32 for x in c]

print(f)

string_comprehension = "Hej"
does_this_work = [x for x in string_comprehension]
print(does_this_work)

int_comperhension = 1234565321432
#does_this = [x for x in int_comperhension]
#print(does_this) #does not
#of course:
int_comperhension = str(int_comperhension)
this_does = [x for x in int_comperhension]
print(this_does)

x = "test"
y = [x for x in range(20)] 
print(y)
print(x) #hashtag scope """

#PART B
""" x = [num for num in range(1, 10)]
y = [num**2 for num in x]

num_square = dict(zip(x, y))

print(num_square) """

""" swag = ["BRA", "JÄTTEBRA", "BÄST", "MYCKET BRA"]
lenswag = [len(word) for word in swag]

swag_lenswag = dict(zip(swag, lenswag))
print(swag_lenswag) """

""" swag = ["BRA", "JÄTTEBRA", "BÄST", "MYCKET BRA", "bra", "BRA", "bäst"]

swaggy = {word.strip().lower() for word in swag}

print(swaggy) """

""" products = {"cool" : 10, "bamam" : 100, "kawawi" : 321, "sssp" : 2309}
cheap_stuff = {k: v for k, v in products.items() if v < 300}
print(cheap_stuff) """

""" students = [
    {"name": "Alve", "score": 100},
    {"name": "Heithem", "score": 10},
    {"name": "Aladdin", "score": 20},
    {"name": "Pelle", "score": 10000},
    {"name": "Erika", "score": 244}
]

passed_students = {
    s["name"]: "PASS" if s["score"] >= 50 else "FAIL" 
    for s in students
}

print(passed_students) """
## PART C
""" songs = ["det går en sjöman på vägen - håkan hellström",
         "song 2 - blur",
         "egen måne - han killen",
         "the chain - fleetwood mac"]

for e, song in enumerate(songs, 1):
    print(e, song) """

""" tasks = ["diska", "gå ut med sopporna", "maila a-kassan", "beställa ny packning till bialetti moka master 6-koppar"]

for e, task in enumerate(tasks, 1):
    print(f"TASK {e}: {task}") """

#values = [123, 345, 64, 77,88, 1, 2, 3, 4, 5, 6, 100, 20, 32]
#
#for e, value in enumerate(values):
#    if value > 25:
#        print(e)

#values = [123, 345, 64, 77,88, 1, 2, 3, 4, 5, 6, 100, 20, 32]
#
#for i in range(len(values)):
#    if values[i] % 2 == 0:
#        print("index:", i, "value :", values[i])
#
#
#for e, value in enumerate(values):
#    if value % 2 == 0:
#        print("index:", e, "value", value)
#
#enumerate gör koden renare eftersom vi slipper manuell indexering (values[i]) i varje iteration.
#Python packar upp både index och värde direkt i loophuvudet. 
#Det minskar risken för fel, gör koden mer lättläst och fungerar på alla typer av dataströmmar (inte bara listor).

##########PART D

#names = ["alve", "heithem", "krille p", "jord", "ando"]
#scores = [123, 321, 423, 234, 543, 345]
#
#student_scores = dict(zip(names, scores))
#
#print(student_scores)

#product = ["bananer", "apelsiner", "citroner", "papaya", "mangoo"]
#price = [10, 20, 30, 10, 20, 30]
#stock = [4, 2, 4, 2, 3, 6]
#
#lager = list(zip(product, price, stock))
#print(lager)

#^different lengths
#data1 = [1, 2, 3, 4, 5]
#data2 = ["a", "b", "c", "d", "e"]
#
#for data_1, data_2 in zip(data1, data2):
#    print(f"data1: {data_1}, data2: {data_2}")
#a = 10
#b = 20
#a, b = b, a
#print(a)
#print(b)
#
#
######## PART E
""" lista = ["alve", "per", "greger", "cassandra", "markus"]

sorted_lista = sorted(lista, key=lambda name: len(name))

print(sorted_lista) """

""" students = [
    {"student" : "alve", "score" : 80},
    {"student" : "zalve", "score" : 70},
    {"student" : "galve", "score" : 90},
    {"student" : "kalve", "score" : 60},
    {"student" : "yalve", "score" : 95},
    ]

print(sorted(students, key=lambda x: x["score"], reverse=True))
print(sorted(students, key=lambda x: x["score"], reverse=False)) """

""" products = [
    {"product" : "alve", "price" : 80},
    {"product" : "zalve", "price" : 70},
    {"product" : "galve", "price" : 90},
    {"product" : "kalve", "price" : 60},
    {"product" : "yalve", "price" : 95},
    ]

print(sorted(products, key=lambda x: x["price"])) """

""" fname_lname = [
    {"fname" : "alve", "lname" : "johansson"},
    {"fname" : "zalve", "lname" : "pohansson"},
    {"fname" : "galve", "lname" : "kohansson"},
    {"fname" : "kalve", "lname" : "wohansson"},
    {"fname" : "yalve", "lname" : "zohansson"},
    ]

print(sorted(fname_lname, key= lambda x: x["lname"], reverse = True)) """

""" fname_lname = [
    {"fname" : "alve", "lname" : "johansson"},
    {"fname" : "zalve", "lname" : "pohansson"},
    {"fname" : "galve", "lname" : "kohansson"},
    {"fname" : "kalve", "lname" : "wohansson"},
    {"fname" : "yalve", "lname" : "zohansson"},
    ]

#regular method = "normal function"?
def get_lastname(person):
    return person["lname"]

sorted_def = sorted(fname_lname, key=get_lastname)

print(sorted_def)

#lambda method? dont really understand the question tbh
sorted_lambda = sorted(fname_lname, key=lambda person: person["lname"])
 """

#### PART F

""" products = [ ##AI generated:
    {"name": "  laptop  ", "category": "ELECTRONICS", "price": "12000", "stock": 4},
    {"name": "mouse", "category": "electronics ", "price": 350.0, "stock": "0"},
    {"name": " KEYBOARD ", "category": "Electronics", "price": 800, "stock": 6},
    {"name": "monitor  ", "category": "electronics", "price": " 3200 ", "stock": 3},
    {"name": "headset", "category": "AUDIO", "price": 950, "stock": "0"},
    {"name": "  webcam ", "category": "electronics", "price": 1100.5, "stock": 5},
    {"name": "MICROPHONE", "category": "audio  ", "price": "1500", "stock": 2},
    {"name": " USB Cable ", "category": "accessories", "price": 150, "stock": "15"},
    {"name": "desk LAMP", "category": " FURNITURE ", "price": " 450 ", "stock": 8},
    {"name": "gaming chair", "category": "furniture", "price": 2500, "stock": "1"},
    {"name": "  hdmi adapter", "category": "ACCESSORIES", "price": "200", "stock": 0},
    {"name": "SPEAKER  ", "category": "Audio", "price": 1800.0, "stock": "4"}
]
 """
""" 
cleaned_products = [
    {
        "name": p["name"].strip().capitalize(),
        "category": p["category"].strip().capitalize(),
        "price": float(p["price"]),
        "stock": int(p["stock"])
    }
    for p in products
]
"""

""" def clean_products(product_list):
    cleaned_list = []
    
    for product in product_list:
        cleaned_item = {
            "name": product["name"].strip().capitalize(),
            "category": product["category"].strip().capitalize(),
            "price": float(product["price"]),
            "stock": int(product["stock"])
        }
        cleaned_list.append(cleaned_item)
        
    return cleaned_list

cleaned_products = clean_products(products)
print(cleaned_products)

in_stock = [product for product in cleaned_products if product["stock"] > 0]
print(in_stock)

unique_categories = {product["category"] for product in cleaned_products}
print(unique_categories)

products_value = {product["name"]: product["price"] * product["stock"] for product in cleaned_products}
print(products_value)

sorted_products = sorted(products_value.items(), key=lambda item: item[1], reverse = True)
print(sorted_products)

print("Highest value list:")
for e, product in enumerate(sorted_products, 1):
    print(f"{e}. {product[0]} with value: {product[1]}")

names = [product["name"] for product in cleaned_products]
stocks = [product["stock"] for product in cleaned_products]

for name, stock in zip(names, stocks):
    print(f"product: {name}, inventory: {stock}")

 """
### for question 9: I don't know if i understand...
### both the list comprehension nad the clean_products function looks alright too me
## I guess you could write something like
# 
#cleaned_bad = [{k: (v.strip().capitalize() if isinstance(v, str) else float(v) if "." in str(v) else int(v)) for k, v in p.items()} for p in products]
# which does not look very readable. IDK.

""" listoflists = [[1, 2, 3], [1, 2, 5], [9, 8, 7]]

flat_list = [num for lista in listoflists for num in lista]
print(flat_list)

nums = [
    {num : num*2}
    for num in range(1, 10)
]
print(nums)
 """

""" multi_table = [[base*factor for base in range(1, 10)] for factor in range(1,10)]

for e, table in enumerate(multi_table, 1):
    print(f"* table of {e}: {table}")

     """

""" names = ["alve", "heithem", "krille p", "jord", "ando"]
scores = [123, 321, 423, 234, 543, 345]

passed_student = [
                    {
                    "name" : name,
                    "score" : score
                   }
                    for name, score in zip(names,scores)
                    if score > 300
                   ]

print(passed_student)

 """

""" scores = [123, 321, 423, 234, 543, 345]

all_passed_loop = True
for score in scores:
    if score <= 100:
        all_passed_loop = False
        break

print(all_passed_loop)

all_passed = all(score > 100 for score in scores)
print(all_passed)

has_score_500 = False
for score in scores:
    if score > 500:
        has_score_500 = True
        break

print(has_score_500)

has_score_500 = any(score > 500 for score in scores)
print(has_score_500) """

##¤¤ 5 exempel på Pythonic syntax

# f-strings
# istället för: "Produkt: " + name + " - Pris: " + str(price)
""" text = f"Produkt: {name} - Pris: {price}" """

# variabelswap
# istället för att skapa en 'temp'-variabel för att byta plats:
""" a, b = b, a """

# enumerate()
# slipper skapa 'i = 0' och plussa på 'i += 1' i loopen:
""" for i, item in enumerate(items, 1):
    print(i, item) """

# any() / all()
# slipper skriva loopar med boolean-flaggor och break:
""" has_stock = any(p["stock"] > 0 for p in products) """

# list / dict Comprehensions
# skapar och filtrerar samlingar direkt istället för tomma listor + .append():
""" in_stock = [p for p in products if p["stock"] > 0] """