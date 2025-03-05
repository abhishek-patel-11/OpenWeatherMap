import requests
import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Configuration (Replace with your own API key and database credentials)
API_KEY = "your_openweathermap_api_key"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "yourpassword",
    "database": "weather_db",
}


def fetch_weather(city):
    """Fetches weather data from OpenWeatherMap API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def save_to_database(city, temperature, description):
    """Saves weather data to MySQL database"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS weather (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(100),
                temperature FLOAT,
                description VARCHAR(255),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        cursor.execute(
            "INSERT INTO weather (city, temperature, description) VALUES (%s, %s, %s)",
            (city, temperature, description),
        )
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")


def get_weather():
    """Handles button click event to fetch and display weather"""
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name")
        return

    data = fetch_weather(city)
    if data:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        result_label.config(
            text=f"Temperature: {temperature}°C\nCondition: {description}"
        )
        save_to_database(city, temperature, description)
    else:
        messagebox.showerror("Error", "Could not retrieve weather data")


# GUI Setup
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x300")

tk.Label(root, text="Enter City:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
