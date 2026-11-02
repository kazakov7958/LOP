import json
import sqlite3

with open("catalog.json", "r", encoding="utf-8") as file:
    items = json.load(file)

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

category_ids = {}

for item in items:
    cat = item["category"]
    cat_name = cat["name"]

    if cat_name not in category_ids:
        cursor.execute(
            "INSERT INTO category (name, description) VALUES (?, ?)",
            (cat_name, cat["description"]),
        )
        category_ids[cat_name] = cursor.lastrowid

    cursor.execute(
        "INSERT INTO product (product_name, price, category_id) VALUES (?, ?, ?)",
        (item["product_name"], item["price"], category_ids[cat_name]),
    )

conn.commit()
conn.close()