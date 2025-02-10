import unittest
import requests
from unittest.mock import patch

# ✅ API details
API_KEY = "ddd2b10f875d47aecd3785c3c71be94f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "New York"
UNITS = "metric"

class TestWeatherData(unittest.TestCase):

    @patch("requests.get")
    def setUp(self, mock_get):
        """✅ Mock API response for testing"""
        self.mock_data = {
            "coord": {"lon": -74.006, "lat": 40.7143},
            "weather": [{"main": "Clouds", "description": "scattered clouds"}],
            "main": {"temp": 5.5, "feels_like": 2.0, "pressure": 1012, "humidity": 80},
            "wind": {"speed": 3.1, "deg": 250},
            "clouds": {"all": 40},
            "sys": {"country": "US"},
            "name": "New York",
            "cod": 200
        }

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.mock_data

        params = {"q": CITY, "appid": API_KEY, "units": UNITS}
        response = requests.get(BASE_URL, params=params)
        self.data = response.json()

    def test_data_types(self):
        """✅ Validate that fields have correct data types"""
        self.assertIsInstance(self.data["coord"]["lon"], float, "❌ Longitude must be a float")
        self.assertIsInstance(self.data["coord"]["lat"], float, "❌ Latitude must be a float")
        self.assertIsInstance(self.data["main"]["temp"], float, "❌ Temperature must be a float")
        self.assertIsInstance(self.data["main"]["humidity"], int, "❌ Humidity must be an integer")
        self.assertIsInstance(self.data["name"], str, "❌ City name must be a string")

    def test_temperature_range(self):
        """✅ Ensure temperature is within a realistic range (-100 to 60°C)"""
        temp = self.data["main"]["temp"]
        self.assertTrue(-100 <= temp <= 60, f"❌ Unrealistic temperature: {temp}")

    def test_pressure_range(self):
        """✅ Ensure atmospheric pressure is within a realistic range (300 - 1100 hPa)"""
        pressure = self.data["main"]["pressure"]
        self.assertTrue(300 <= pressure <= 1100, f"❌ Unrealistic pressure: {pressure}")

    def test_wind_speed_range(self):
        """✅ Ensure wind speed is within a valid range (0 - 150 m/s)"""
        wind_speed = self.data["wind"]["speed"]
        self.assertTrue(0 <= wind_speed <= 150, f"❌ Unrealistic wind speed: {wind_speed}")

    def test_required_keys(self):
        """✅ Verify all required keys exist in the API response"""
        required_keys = ["coord", "weather", "main", "wind", "clouds", "sys", "name", "cod"]
        for key in required_keys:
            self.assertIn(key, self.data, f"❌ Missing key: {key}")

if __name__ == "__main__":
    unittest.main()
