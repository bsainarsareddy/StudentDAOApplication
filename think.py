import sqlite3
import csv


conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
)
""")


with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
        INSERT INTO products (id, name, category, price, stock)
        VALUES (?, ?, ?, ?, ?)
        """, (row['id'], row['name'], row['category'], row['price'], row['stock']))

conn.commit()
conn.close()

