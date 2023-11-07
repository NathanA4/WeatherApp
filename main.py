import ttkbootstrap
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = ttkbootstrap.Window(themename="morph")
root.title("APP")
root.geometry("200x200")

cityEntry = ttkbootstrap.Entry(root, font="Helvetic, 20")
cityEntry.pack(pady=10)

searchButton = ttkbootstrap.Button(root, text="Seach", command=search, bootstyle="warning")
searchButton.pack(pady=10)

loactionLabel = tkk.Label(root, font="Helvetic, 25")
loactionLabel.pack(pady=10)

iconLabel = tk.Label(root)
iconLabel.pack()

tempLabel = tk.Label(root, font="Helvetica, 20")
tempLabel.pack()

descriptionLabel = tk.Label(root, font="Helvetica, 20")
descriptionLabel.pack()

def userinput():
    city = cityEntry.get()
    result = getWeather(city)
    if result is None:
        return

def getWeather(city):
    APIKEY = ""
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}lat={lat}&lon={lon}&appid={APIKEY}"
    REQUEST = requests.get(url)
