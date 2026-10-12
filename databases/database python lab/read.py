import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

print(rows)

conn.close()