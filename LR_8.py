import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON ;")
cursor.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount REAL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
""")

cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM customers")


cursor.executemany("INSERT INTO customers(name) VALUES (?)", [
    ("Ivan",),
    ("Peter",),
    ("Kolya",),
    ("Serj",),
])


cursor.executemany("INSERT INTO orders(customer_id, amount) VALUES (?, ?)", [
    (3, 100500),
    (1, 100.5),
    (4, 123),
    (2, 246),
    (1, 369.5),
    (999, 66.6)
])

conn.commit()
conn.close()
