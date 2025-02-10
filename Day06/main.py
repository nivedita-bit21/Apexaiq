import requests
import json

# ✅ Replace with your actual API key
API_KEY = "ddd2b10f875d47aecd3785c3c71be94f"

# ✅ Free API URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ✅ City name (e.g., New York)
CITY = "New York"
UNITS = "metric"  # "imperial" for Fahrenheit

# ✅ API request parameters
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": UNITS
}

# ✅ Make API request
response = requests.get(BASE_URL, params=params)

# ✅ Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # ✅ Save response to a JSON file
    with open("weather_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("\n🔹 Weather Report for", data["name"], f"({data['sys']['country']})")
    print(f"🌡️ Temperature: {data['main']['temp']}°C (Feels like {data['main']['feels_like']}°C)")
    print(f"💨 Wind Speed: {data['wind']['speed']} m/s, Direction: {data['wind']['deg']}°")
    print(f"☁️ Cloud Cover: {data['clouds']['all']}%")
    print(f"🌍 Coordinates: {data['coord']['lat']}, {data['coord']['lon']}")

    print("\n✅ Data saved to **weather_data.json** successfully!")
else:
    print(f"❌ Error {response.status_code}: {response.json()['message']}")
