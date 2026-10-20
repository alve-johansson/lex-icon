from pymongo import MongoClient
from pprint import pprint
import datetime as dt

client = MongoClient("localhost", 27017)  # eller MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

#for product in db.products.find({"category": "Accessories"}):
#    print(product.get("name"))

#for customer in db.customers.find({"city": "Göteborg"}):
#    print(customer.get("first_name"), customer.get("last_name"))

#for product in db.products.find():
#    print(product.get("name"), product.get("price"))

#count = db.customers.count_documents({"city": "Uppsala"})
#print(count)

#product = db.products.find_one({"name": "Sandals"})
#if product:
#    print(product.get("stock"))

#for customer in db.customers.find({"newsletter": True}):
#    print(customer.get("first_name"))

""" new_customer = {
    "first_name": "Alve",
    "last_name": "Johansson",
    "email": "alvepython2026@outlook.com",
    "city": "Götlaborg"
}

result = db.customers.insert_one(new_customer)
print(result.inserted_id)

found = db.customers.find_one({"email": "alvepython2026@outlook.com"})
pprint(found) """

""" new_products = [
    {"_id": 13, "name": "Product 13", "category": "Test", "price": 100, "stock": 10, "tags": ["new"]},
    {"_id": 14, "name": "Product 14", "category": "Test", "price": 150, "stock": 5, "tags": ["sale"]}
]

db.products.insert_many(new_products)
print(db.products.count_documents({})) """

#for customer in db.customers.find():
#    first = customer.get("first_name", "")
#    last = customer.get("last_name", "")
#    city = customer.get("city", "(Unknown)")
#    print(f"{first} {last} ({city})")

#for order in db.orders.find():
#    order_id = order.get("_id")
#    items_count = len(order.get("items", []))
#    print(f"Order {order_id}: {items_count} items")

#for product in db.products.find({"price": {"$gt": 1000}}):
#    pprint(product.get("name"))

#for order in db.orders.find({"status": {"$ne": "delivered"}}):
#    order_id = order.get("_id")
#    order_status = order.get("status")
#    pprint(f"{order_id} and {order_status}")

#for customer in db.customers.find({"city": {"$in": ["Malmö", "Stockholm"]}}):
#    customer_name = customer.get("first_name")
#    customer_name += customer.get("last_name")
#    pprint(f"hello {customer_name}")

#for product in db.products.find({"details.color" : "white"}):
#    print(product.get("name"))

#for product in db.products.find({"tags": "sport"}):
#    name = product.get("name")
#    tags = product.get("tags")
#    print(f"{name} with tags: {tags}")

#for product in db.products.find().sort("price", 1).limit(5):
#    name = product.get("name")
#    price = product.get("price")
#    print(f"product: {name}, price: {price} kr")

#for order in db.orders.find({"items.product_id" : 2 }):
#    order = order.get("_id")
#    print(order)


#db.products.update_many({"category": "Accessories"}, {"$inc": {"price": -20}})


#for product in db.products.find({"category": "Accessories"}):
#    price = product.get("price")
#    name = product.get("name")
#    print(f"product name: {name} --- product new price {price}")

#db.products.update_one(
#    {"name": "Rain Jacket"}, 
#    {"$set": {"tag": "new", "restock_date": dt.datetime.now()}}, 
#    upsert=True
#)



""" print(db.orders.count_documents(
    {
    "status": "new", 
    "order_date": {"$lt": dt.datetime(2026, 3, 20)}
    }
                                )
    )

db.orders.delete_many(
    {
    "status": "new", 
     "order_date": {"$lt": dt.datetime(2026, 3, 20)}
     }
  """                       #)
""" 
print(db.orders.count_documents(
    {
    "status": "new"
    }
                                )
    )
 """
