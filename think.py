import sqlite3
import csv

# Connect to SQLite DB (or create it)
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
)
""")

# Load CSV and insert data
with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
        INSERT INTO products (id, name, category, price, stock)
        VALUES (?, ?, ?, ?, ?)
        """, (row['id'], row['name'], row['category'], row['price'], row['stock']))

conn.commit()
conn.close()

