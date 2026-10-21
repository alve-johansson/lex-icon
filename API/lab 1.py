from api_client import get_json
import pprint
import os
from dotenv import load_dotenv
import requests


base_url = "https://fakestoreapi.com/"


""" response = get_json("https://fakestoreapi.com/products")

print(type(response))

sorted_response = sorted(response, key=lambda x: x['price'])

for data in sorted_response:
    print(f"!! {data['title']} is da bomb price ya: {data['price']}")
 """

""" categories = get_json(base_url + "products/categories")

choice = input('What category do you want?').strip()

if choice not in categories:
    print("ERROR invalid cateogry")
else:
    products_in_category = get_json(base_url + "products/category/" + choice)
    
    if not products_in_category:
        print(f"CATEGORY EXIST '{choice}' BUT IS EMPTY.")
    else:
        print(f"NUMBER OF PRODUCTS: {len(products_in_category)}")
        sorted_products_in_category = sorted(products_in_category, key= lambda x: x['price'])
        print(f"{sorted_products_in_category[0]['title']} for ${sorted_products_in_category[0]['price']}") """

""" new_product = [
    {"title" : "test"},
    {"price" : "test"},
    {"description" : "test"},
    {"image" : "test"},
    {"category" : "test"}
]

response = requests.post("https://fakestoreapi.com/products", json=new_product)

print(response)
print(response.status_code)

response = requests.patch("https://fakestoreapi.com/products/7", json={'price': 49.0})

print(response.status_code)
print(response.json()) """

""" response = get_json(base_url + "blablablablblbal")
print(response)

response = get_json(base_url, timeout = 0.0001)
print(response)

response = get_json("https://hello.alvej.dev")
print(response)

response = get_json("https://github.com/admin")
print(response) """