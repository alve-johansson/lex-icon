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
lista = ["alve", "per", "greger", "cassandra", "markus"]

sorted_lista = sorted(lista, key=lambda name: len(name))

print(sorted_lista)