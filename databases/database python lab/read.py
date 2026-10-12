import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

cursor.execute("SELECT name, price FROM products")
rows = cursor.fetchall()

print(rows)

conn.close()