import requests

WEATHER_CODES = {
    0: "☀️ Ясно",
    1: "🌤️ Преимущественно ясно",
    2: "⛅ Переменная облачность",
    3: "☁️ Пасмурно",
    45: "🌫️ Туман",
    48: "🌫️ Иней",
    51: "🌦️ Легкая морось",
    53: "🌦️ Морось",
    55: "🌧️ Сильная морось",
    61: "🌧️ Небольшой дождь",
    63: "🌧️ Дождь",
    65: "🌧️ Сильный дождь",
    71: "🌨️ Небольшой снег",
    73: "🌨️ Снег",
    75: "🌨️ Сильный снег",
    80: "🌦️ Ливень",
    95: "⛈️ Гроза",
    96: "⛈️ Гроза с градом",
}

city_name = str(input("Введите название города (eng): "))
if city_name.strip() == "":
    print("Поле не должно оставаться пустым!")
    exit()


def get_city_coordinates(city_name):
    link_1 = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=ru"
    get_data_LL = requests.get(link_1)
    data_LL = get_data_LL.json()
    if not data_LL.get("results"):
        print(f"Город '{city_name}' не найден. Проверьте название.")
        return None
    lat = data_LL["results"][0]["latitude"]
    lon = data_LL["results"][0]["longitude"]
    return lon, lat


def get_weather(lon, lat):
    link_2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
    get_data_weather = requests.get(link_2)
    data_weather = get_data_weather.json()
    tmp = data_weather["current"]["temperature_2m"]
    hmd = data_weather["current"]["relative_humidity_2m"]
    wc = data_weather["current"]["weather_code"]
    return tmp, hmd, wc


coords = get_city_coordinates(city_name)
if coords is None:
    exit()

lon, lat = coords
tmp, hmd, wc = get_weather(lon, lat)

condition = WEATHER_CODES.get(wc, f"Неизвестные условия (код: {wc})")

print(f"Погода в городе: {city_name}")
print(f"Температура:  {tmp:+.1f}°C")
print(f"Влажность:     {hmd}%")
print(f"Ветер:         {wc} км/ч")
print(f"Состояние:    {condition}")
