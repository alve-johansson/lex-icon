# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
""" def product_names(products):
    for product in products:
        if product["stock"] > 0:
            print(product["name"])

    return

product_names(products)

def value_in_stock(products):
    total_value = 0

    for product in products:
        if product["stock"] > 0:
            total_value += product["stock"]*product["price"]

    return total_value

print(value_in_stock(products))

def highets_price(products):
    highest_priced_product_price = 0
    highest_priced_product_name = ""
    for product in products:
        if product["price"] > highest_priced_product_price and product["stock"] > 0:
            highest_priced_product_price = product["price"]
            highest_priced_product_name = product["name"]

    return highest_priced_product_price, highest_priced_product_name

print(highets_price(products)) """

# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
""" 
def calculate_average(scores):
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1

    avg = total/count
    return avg

def create_result(scores):
    return "PASS" if calculate_average(scores) >= 70 else "FAIL"

print(calculate_average(scores))
print(create_result(scores)) """


# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

""" def calculate_order(customer_name, *product_prices, **optional_settings):
    total_product_cost = 0
    reduced_product_cost = 0
    final_cost = 0
    discount = optional_settings.get("discount", 0)
    shipping = optional_settings.get("shipping", 0)

    for product_price in product_prices:
        total_product_cost += product_price

    discount = (100-discount)/100
    reduced_product_cost = total_product_cost * discount
    final_cost = reduced_product_cost + shipping

    return {"customer" : customer_name, "subtotal" : total_product_cost, "final_total" : final_cost, "settings" : optional_settings}

product_prices = [100, 200, 300, 400]
order_settings = {"discount" : 30, "shipping" : 50}

print(calculate_order("Anna", *product_prices, **order_settings))
 """


# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
""" 
nomalised_players = [player["name"].strip().capitalize() for player in players]
print(nomalised_players)
 """""" 
active_players = [player for player in players if player["score"] > 79 and player["active"] == True]
print(active_players)
 """
""" print(sorted(players, key=lambda x: x["score"], reverse=True)) """

""" players = sorted(players, key=lambda x: x["score"], reverse=True)

for e, player in enumerate(players, 1):
    print(f"{e}. {player["name"].strip().capitalize()} - {player["score"]}") """

""" score_list = [player["score"] for player in players]
name_list = [player["name"] for player in players]

print(score_list, name_list)

for player in zip(name_list, score_list):
    print(f"player: {player[0]} - score: {player[1]}")
 """