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

