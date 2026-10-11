import json

with open("students_db.json", "r", encoding="utf-8") as f:
    students = json.load(f)

print("Активные студенты:")


for student in students:
    if student["is_active"]:
        print(student["name"])
