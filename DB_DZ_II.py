import json
import sqlite3

with open("catalog.json", "r", encoding="utf-8") as file:
    itms = json.load(file)

conn = sqlite3.connect("database.db")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        price REAL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES category (id)
    )
""")

cursor.execute("DELETE FROM product")
cursor.execute("DELETE FROM category")

category_id = {}

for itm in itms:
    categ = itm["category"]
    categ_name = categ["name"]

    if categ_name not in category_id:
        cursor.execute(
            "INSERT INTO category (name, description) VALUES (?, ?)",
            (categ_name, categ["description"]),
        )
        category_id[categ_name] = cursor.lastrowid

    cursor.execute(
        "INSERT INTO product (product_name, price, category_id) VALUES (?, ?, ?)",
        (itm["product_name"], itm["price"], category_id[categ_name]),
    )

conn.commit()
conn.close()    