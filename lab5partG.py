#LAB 5 PART G

#1
""" def merge_settings(defaults, **overrides):
    return {**defaults, **overrides}

default_cfg = {"theme" : "light", "font_size" : 12, "font" : "Arial"}
user_cfg = merge_settings(default_cfg, theme = "dark", font_size = 12, font = "Times New Roman")

print(user_cfg)
print(default_cfg) """

#2
""" def call_summary(function_name, *args, **kwargs):
    return f"Calling function '{function_name}' with args: {args} and kwargs: {kwargs}"

print(call_summary("calculate_fee", "bananer", 100, "usd", 50, True, role="admin", shipping = "free")) """


#3
""" def statistics(*numbers):
    if len(numbers) == 0:
        return 0, 0, 0, None, None

    total = 0
    count = 0
    num_min = numbers[0]
    num_max = numbers[0]

    for num in numbers:
        total += num
        count += 1
        if num < num_min:
            num_min = num
        if num > num_max:
            num_max = num

    avg = total / count
    return count, total, avg, num_min, num_max

lista = [1, 2, 3, 4, 5, 6, 6, 6, 6, 1, 1, 1, 1, 1]

print(statistics(*lista)) """

#4
""" x = 10
def test():
    x = 20000
    return x
test()
print(x) #10

bananer = 200
def test2():
    bananer = 300
    def test22():
        print(bananer) #300

print(bananer) #200

a = 10
b = 20
a = b
z = 100
def b_to_a(y):
    y = z
    return y

b_to_a(a)


f = 10

def f_to_200(p):
    p = 200
    return p

f = f_to_200(f)
print(f) """

""" x = 100

def global_buffe():
    global x
    x = 200

print(x)
global_buffe()
print(x)
 """
