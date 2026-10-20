""" conn = sqlite3.connect("databases/database python lab/webshop.db")
cursor = conn.cursor()

##cursor.execute("SELECT count(*) FROM customers")
##count = cursor.fetchone()[0]
cursor.execute("SELECT first_name, last_name,city FROM customers")
print(cursor.fetchall())

conn.close()
 """

""" conn = sqlite3.connect("databases/database python lab/webshop.db")
cursor = conn.cursor()

##cursor.execute("SELECT count(*) FROM customers")
##count = cursor.fetchone()[0]
max_price = input()

cursor.execute("SELECT name, price FROM products WHERE price < ?", (max_price,))
print(cursor.fetchall())

conn.close()
 """
""" conn = sqlite3.connect("databases/database python lab/webshop.db")
cursor = conn.cursor()

##cursor.execute("SELECT count(*) FROM customers")
##count = cursor.fetchone()[0]
category = input()

cursor.execute("SELECT count(*) FROM products WHERE category = ?", (category,))
print(cursor.fetchone())

conn.close() """
## f-string can be used for sql injection. Never ever ever use f-string to sql.
## the ? thing is OLNY interpered as string not code
import sqlite3


def connect():
    conn = sqlite3.connect("databases/database python lab/webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def change_stock(conn):
    new_stock = int(input("New stock: ..."))
    product_id_cs = int(input("What product id: ..."))
    
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (new_stock, product_id_cs)
    )
    conn.commit()
    print("Saved!")

def show_receipt(conn):
    order_id = int(input("PLEASE TELL ME ORDER ID"))
    
    conn.execute('''SELECT o.order_id, c.first_name, c.last_name, o.order_date, p.name, oi.quantity, p.price, (p.price*oi.quantity) AS line_total
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id
        WHERE o.order_id = ?;''',
        (order_id)
    )
    conn.commit()
    print("Saved!")

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product 4) Change stock 0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)                    
        elif choice == "0":
            break
    conn.close()


main()
