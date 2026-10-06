## Пример I
``` python
import json

def load_config (file_path):

file = None

try :

# 1. ЗОНА РИСКА: только открытие и чтение

file = open(file_path, 'r', encoding='utf-8')

raw_data = file.read()

except FileNotFoundError as e:

#2. СПАСЕНИЕ: обрабатываем конкретную ошибку

print (f'[ERROR] Конфиг не найден по пути {file_path}.Используем дефолтный.")

return {'timeout': 30}

except json. JSONDecodeError as e:

#3. СПАСЕНИЕ: обрабатываем ошибку парсинга 
print (f" [ERROR] Файл поврежден. Ошибка парсинга: {e}") 
raise # Пробрасываем ошибку дальше, так как конфиг критичен

else:
# 4. ПУТЬ СЧАСТЬЯ: выполняется, если try прошел успешнo
# Если здесь будет опечатка (например, jason. loads), # она не перехватится блоком except выше, а упадет честно.

config = json. loads (raw_data)

print (" (INFO) Конфиг успешно загружен.")

return config

finally:

# 5. УБОРЩИК: закроем файл в любом случае

if file is not None:

file. close ()
print ("(DEBUG) Файл конфигурации закрыт.)
```

## Пример II
```python
def set_age(age):
    if age < 0:
        raise ValueError("out of range")
```

## Пример III.I
```python
except ConnectionError as e:
	logging.error("Ошибка сети")
	raise ConnectionError("Ошибка сети")
```

## Пример III.II
*Более верный способ*
```python
except ConnectionError:
	logging.error("Ошибка сети")
	raise
```

## Пример IV
```python
class BaseParser:
	def parse(self,data):
		raise NotImplementedEror(f 'Класс {self.__class__.__name__ должен реализовать метод parse')
```

## Пример V
### Начало работы с JSON
```python
import json

data = {'name' : 'Иван',
		'is_student' : True,
		'grades':[4,5,5]}
json_string = json.dumps(data, ensure_ascii = False)

parsed_data = json.loads(json_string)
```

## Пример VI
### Запись в файл JSON
```python
with open("data.json", "w", encoding = 'utf-8') as f:
	json.dump(data, f, ident = 4, ensure_ascii = False)
```

## Пример VII
```python
with open ("data.json", 'r', encodig = 'utf-8') as f:
	loaded_data = json.load(f)
```

##  Пример VIII
*Засунем в класс*
```python
import json
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age
stud = Student("Петр", 19)
def student_to_dict(obj):
	if isinstance(obj, Student):
		return {"name": obj.name, "age":obj.age, "type": "Student"}
	raise TypeError("Unknow object type")
json_str = json.dumps(stud, default = student_to_dict)

with open("json_str", "w", encoding = 'utf-8') as f:
	json.dump(json_str, f, ident = 4, ensure_ascii = False)

```

## Пример IX

*Создадим файл **Students_db.json***
```json
{'id': 1, "name": "Алексей", "group": "ИУ 10-33", "schoolarship": 1000, "is_active": true},
{'id': 2, "name": "Мария", "group": "ИУ 10-35", "schoolarship": 2000, "is_active": true},
{'id': 3, "name": "Дмитрий", "group": "ИУ 10-33", "schoolarship": null, "is_active": false},
{'id': 4, "name": "Елена", "group": "ИУ 10-36", "schoolarship": 5000, "is_active": true}
```

```python
import json

with open("students_db.json", "r", encoding="utf-8") as f:
    students = json.load(f)

print("Активные студенты:")


for student in students:
    if student["is_active"]:
        print(student["name"])

```

