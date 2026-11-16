import os
import requests

noj = 9


try:

    name = input("Введите имя цели: ").strip()

    r_age = requests.get("https://api.agify.io", params={"name": name}).json()
    age = r_age.get("age")
    if age is None:
        print(f"Agify не знает имя '{name}'. Попробуйте другое (например, 'Sergei').")
        exit()

    g = requests.get("https://api.genderize.io", params={"name": name}).json()
    if g.get("gender") is None:
        print(f"Genderize не знает имя '{name}'.")
        exit()

    f_prob = g["probability"] * 100 if g["gender"] == "female" else 100 - g["probability"] * 100
    print(f"Цель: {name}. Вероятный возраст: {age}. Вероятность женского пола: {f_prob:.0f}%.")

   
    hdr = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) СекретныйАгентБот/1.0".encode().decode("latin-1"),
        "Accept-Language": "ru-RU,ru;q=0.9",
    }
    posts = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": noj},
        headers=hdr,
    ).json()
    print("Количество постов:", len(posts))
    print("Заголовок первого поста:", posts[0]["title"])

   
    data = {"name": name, "age": age, "gender": g["gender"], "posts_count": len(posts)}
    print("Принятый сервером JSON:",
          requests.post("https://httpbin.org/post", json=data).json()["json"])


    img = requests.get("https://picsum.photos/400/300", stream=True)
    with open("evidence.jpg", "wb") as f:
        f.write(img.content)
    print("Размер файла в байтах:", os.path.getsize("evidence.jpg"))

except requests.exceptions.RequestException as e:
    print("Сетевая ошибка:", e)
    exit()


try:
    requests.get("https://httpbin.org/status/404").raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Сервер ответил ошибкой:", e)

try:
    requests.get("https://httpbin.org/delay/6", timeout=3)
except requests.exceptions.Timeout:
    print("Сервер не ответил за 3 секунды.")
