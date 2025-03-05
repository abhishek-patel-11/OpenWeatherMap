# 🌦 Weather Dashboard Application

A **Python-based Weather Dashboard** that retrieves real-time weather data using the **OpenWeatherMap API**, displays it via a **Tkinter GUI**, and stores historical weather information in a **MySQL database**. This application is designed for quick and easy weather monitoring with a user-friendly interface.

## 🚀 Project Overview

This project is a simple yet powerful **Weather Dashboard** that allows users to fetch **current weather conditions** for any city in the world. The application seamlessly integrates **API calls, GUI interaction, and database storage** to provide a comprehensive weather tracking experience.

### 🔹 Key Features
- **Real-time Weather Fetching**: Retrieves live weather data from OpenWeatherMap.
- **Graphical User Interface (GUI)**: Built with **Tkinter** for an intuitive user experience.
- **Database Storage**: Saves weather details in a **MySQL database** for future reference.
- **Error Handling**: Manages API failures and incorrect city inputs gracefully.
- **Multi-city Support**: Users can check the weather of multiple locations.

## 📦 Installation & Setup

Follow these steps to set up and run the project on your local system:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/Weather-Dashboard.git
cd Weather-Dashboard
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then run the following command to install required packages:
```sh
pip install requests mysql-connector-python tkinter
```

### 3️⃣ Set Up MySQL Database
1. **Open MySQL** and create a new database:
   ```sql
   CREATE DATABASE weather_db;
   ```
2. **Modify Database Credentials** in `WeatherMap.py`:
   ```python
   DB_CONFIG = {
       "host": "localhost",
       "user": "root",
       "password": "yourpassword",
       "database": "weather_db"
   }
   ```
3. The required database table is **automatically created** when the script is executed.

## 🎯 Usage

To run the Weather Dashboard, execute:
```sh
python WeatherMap.py
```
- **Step 1**: Enter a **city name** in the input field.
- **Step 2**: Click **"Get Weather"** to fetch data.
- **Step 3**: The app displays **temperature and weather conditions**.
- **Step 4**: The data is automatically **saved to the database** for future reference.

## 🖥 Example Output

**GUI Output:**
```
City: New York  
Temperature: 22°C  
Condition: Clear Sky  
```

## 🔧 Troubleshooting

1️⃣ **API Key Error?**  
- Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api) and update `API_KEY` in the script.

2️⃣ **Database Connection Issues?**  
- Ensure **MySQL is running**, and the credentials are correctly set in `WeatherMap.py`.

3️⃣ **Missing Modules?**  
- Install dependencies using:
  ```sh
  pip install -r requirements.txt
  ```

## 🤝 Contributing

Contributions are welcome! If you have any suggestions, feel free to fork this repository and submit a pull request.

## 📜 License

This project is licensed under the **MIT License**.


