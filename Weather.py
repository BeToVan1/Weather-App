import requests
import tkinter as tk
from tkinter import PhotoImage

def fetch_weather():
    api_key = '08f421c33bb34dc49e101541230408'
    base_url = 'http://api.weatherapi.com/v1/forecast.json'
    location = location_entry.get()

    url = f'{base_url}?key={api_key}&q={location}&days=7'  # Fetch 7-day forecast

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        current_temp = weather_data['current']['temp_f']
        current_condition = weather_data['current']['condition']['text']
        current_humidity = weather_data['current']['humidity']

        image_path = "sunny.png"

        # Load image based on condition
        if "sunny" in current_condition:
            image_path = "sunny.png"

        weather_icon = PhotoImage(file=image_path)
        resized_icon = weather_icon.subsample(6,6)
        icon_label.config(image=resized_icon)
        icon_label.image = resized_icon

        # Display current weather information
        weather_info = f'Temperature: {current_temp}°F\nCondition: {current_condition}\nHumidity: {current_humidity}%'
        weather_label.config(text=weather_info)

        # Get daily forecasts
        daily_forecasts = weather_data['forecast']['forecastday']

        # Display weekly weather forecast information
        weekly_info = "Weekly Forecast:\n"
        for day in daily_forecasts:
            date = day['date']
            max_temp = day['day']['maxtemp_f']
            min_temp = day['day']['mintemp_f']
            condition = day['day']['condition']['text']
            weekly_info += f"{date}: Min Temp: {min_temp}°F, Max Temp: {max_temp}°F, Condition: {condition}\n"

        weekly_label.config(text=weekly_info)

    else:
        weather_label.config(text='Error: Failed to fetch weather data.')
        weekly_label.config(text='')

# Create a Tkinter application
app = tk.Tk()
app.title("Weather App")
app.geometry("700x500")

# Change the background color of the main window
app.configure(bg="lightblue")

# Label for displaying current weather information
weather_label = tk.Label(app, text="Weather Information", font=("Helvetica", 14), bg="lightblue")
weather_label.pack(pady=10)

# Label to display the weather icon
icon_label = tk.Label(app, image=None, bg="lightblue")
icon_label.pack(pady=10)

# Entry field for the location
location_entry = tk.Entry(app, font=("Helvetica", 12))
location_entry.pack(pady=10)

# Button to fetch weather information
fetch_button = tk.Button(app, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

# Label for displaying weekly weather forecast information
weekly_label = tk.Label(app, text="Weekly Forecast:", font=("Helvetica", 12), bg="lightblue", justify="left", anchor="center")
weekly_label.pack(pady=10)

app.mainloop()
