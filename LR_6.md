# **БАЗЫ ДАННЫХ**
# SQL. CRUD. СУБД
СУБД - системы управления базами данных.

*ID будет увеличиваться автоматически увеличиваться на единицу при внесении данных, его как правило не указываем.*

| id  | name   | mark | age |
| --- | ------ | ---- | --- |
| 1   | Иванов | 41   | 19  |
|     |        |      |     |
|     |        |      |     |

```sql
CREATE TABLE students(
	id INTEGER PRIMARY KEY,
	name TEXT,
	mark REAL,
	age INTEGER)
#ввод данных первой строки
INSERT INTO students(name, mark, age) VALUES ('Иванов', 41,19)
#ищем студентов старше 18 лет
SELECT * FROM students WHERE age > 18

#обновляем данные первой строки
UPDATE students SET age = 20 WHERE name = 'Иванов'

#удаляем первую строку(впринципе не важно какую)
DELETE FROM students WHERE id = 1 
```

```python
import sqlite3
conn = sqlite3.connect("univercity.db")
cursor = conn.cursor()
cursor.execute('CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, mark REAL, age INTEGER)')
```

***Дальше DB Browser для SQLite:***![[Screenshot 2026-10-13 at 17.20.55.png]]

***Заметим, если мы захотим изменить или перезаписать файл, то терминал выдаст ошибку***
```python
import sqlite3
conn = sqlite3.connect("univercity.db")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, mark REAL, age INTEGER)')
```

***Работаем дальше, напишем три функции для создания таблицы, добавления данных и их удаления, обновления по id***
```python
import sqlite3
def create_tbl():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, mark REAL, age INTEGER)')
    conn.commit()
    conn.close()

 create_tbl()   

def insert_into():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(name, mark, age) VALUES ('Иванов', 41,19)")
    conn.commit()
    conn.close()

insert_into()

def delete():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = 1")
    conn.commit()
    conn.close()

delete()

def update_info():
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET age = 25 WHERE id = 3")
    conn.commit()
    conn.close()

update_info()
```

***Напишем функцию для добавления значений произвольным образом***
```python
def insert_into(name1, mark1, age1):
    conn = sqlite3.connect("univercity.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, mark, age)
        VALUES (?, ?, ?)''', (name1, mark1, age1))
    conn.commit()
    conn.close()

insert_into('Иванов', 48, 93)
```

***Одна команда - много данных***
```python
cursor.executemany("INSERT NTO students (name, mark, age) VALUES (?, ?, ?), data")
data=[("Фамилия_1", 5, 2)("Фамилия_2",4,9)("Фамилия_3", 80,90)]
```

***Принципы ACID:***
1. Атомарность
2. Согласованность
3. Изолированность
4. Долговечность