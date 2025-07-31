import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("SELECT DISTINCT department FROM products")
unique_departments = cursor.fetchall()


for dep in unique_departments:
    cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", (dep[0],))

conn.commit()
conn.close()
