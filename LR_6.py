import sqlite3
def create_tbl():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, mark REAL, age INTEGER)')
    conn.commit()
    conn.close()

 

def insert_into():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(name, mark, age) VALUES ('Иванов', 41,19)")
    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = 1")
    conn.commit()
    conn.close()

def update_info():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET age = 25 WHERE id = 3")
    conn.commit()
    conn.close()

update_info()
