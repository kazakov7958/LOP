import json
with open("users.json", encoding="utf-8") as f:
    users = json.load(f)

group = {}
for user in users:
    user_group = user["address"]["city"]
    if user_group not in group:
        group[user_group] = []
    group[user_group].append(user["name"])

with open("cities.json", "w", encoding="utf-8") as f:
    json.dump(group, f, ensure_ascii=False, indent=2)

print(group)
