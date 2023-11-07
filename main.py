import ttkbootstrap
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def userinput():
    city = cityEntry.get()
    result = getWeather(city)
    if result is None:
        return
    iconURL, description, temp, city, country = result
    locationLabel.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(iconURL, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    iconLabel.configure(image=icon)
    iconLabel.image = icon

    tempLabel.configure(text=f"Temperature: {temp:.2f}°C")
    descriptionLabel.configure(text=f"Description: {description}")
    
root = ttkbootstrap.Window(themename="morph")
root.title("APP")
root.geometry("200x200")

cityEntry = ttkbootstrap.Entry(root, font="Helvetica 20")
cityEntry.pack(pady=10)

searchButton = ttkbootstrap.Button(root, text="Search", command=userinput, bootstyle="warning")
searchButton.pack(pady=10)

locationLabel = ttkbootstrap.Label(root, font="Helvetica 25")  # Corrected typo
locationLabel.pack(pady=10)

iconLabel = tk.Label(root)
iconLabel.pack()

tempLabel = tk.Label(root, font="Helvetica 20")
tempLabel.pack()

descriptionLabel = tk.Label(root, font="Helvetica 20")  # Corrected typo
descriptionLabel.pack()



def getWeather(city):
    APIKEY = "14820d48f26f136e2da6ed36da9dc80c"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}"  # Removed lat and lon from the URL
    REQUEST = requests.get(URL)  # Corrected variable name

    if REQUEST.status_code == 404:
        messagebox.showerror("ERROR City Not Found!")
        return None
    weather = REQUEST.json()
    iconId = weather['weather'][0]['icon']
    temp = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    iconURL = f"https://openweathermap.org/img/wn/{iconId}@2x.png"  # Corrected URL format
    return (iconURL, description, temp, city, country)

root.mainloop()
