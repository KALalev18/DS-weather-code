import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API key not found. Please check your .env file.")
    exit()

while True:
    city = input("Enter the city name: ").strip()

    if not city:
        print("City name cannot be empty. Please try again.")
        continue

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C")
        break
    elif data.get("message") == "city not found":
        print("Invalid city name. Please enter a valid city.")
    else:
        print("Error fetching weather data:", data)
        break
