import sqlite3

conn = sqlite3.connect("accounts.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER PRIMARY KEY, name TEXT, balance INTEGER)")
raise exception("!!!Power Failure!!!")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Kolya', 1500)")
cursor.execute("INSERT INTO accounts(name, balance) VALUES ('Petya', 2500)")

cursor.execute("UPDATE accounts SET balance = balance - 1000 WHERE id = 1")
cursor.execute("UPDATE accounts SET balance = balance + 1000 WHERE id = 2")

conn.commit()
conn.close()
