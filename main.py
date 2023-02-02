import tkinter as tk
import requests

def get_weather(city):
    weather_key = "2e14ce4f40cd08817a04bc37e4262cbe"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "APPID": weather_key,
        "q": city,
        "units": "metric",
    }
    response = requests.get(url, params=params)
    weather = response.json()
    if "message" in weather:
        label["text"] = "City not found"
    else:
        temperature = weather["main"]["temp"]
        description = weather["weather"][0]["description"]
        label["text"] = f"Temperature: {temperature:.1f}°C, {description}"

root = tk.Tk()
root.title("Weather")

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Get weather", command=lambda: get_weather(entry.get()))
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()
