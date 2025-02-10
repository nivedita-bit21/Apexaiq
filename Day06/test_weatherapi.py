import unittest
import requests
from unittest.mock import patch

# ✅ API details
API_KEY = "ddd2b10f875d47aecd3785c3c71be94f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "New York"
UNITS = "metric"


class TestWeatherAPI(unittest.TestCase):

    def test_api_response(self):
        """✅ Test if the API returns a valid response (status code 200)"""
        params = {"q": CITY, "appid": API_KEY, "units": UNITS}
        response = requests.get(BASE_URL, params=params)
        self.assertEqual(response.status_code, 200, "❌ API request failed!")

    def test_json_structure(self):
        """✅ Test if the JSON response contains the required keys"""
        params = {"q": CITY, "appid": API_KEY, "units": UNITS}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        required_keys = ["coord", "weather", "main", "wind", "clouds", "sys", "name", "cod"]
        for key in required_keys:
            self.assertIn(key, data, f"❌ Missing key: {key}")

    @patch("requests.get")
    def test_mocked_api_response(self, mock_get):
        """✅ Test with mocked API response to avoid real API calls"""
        mock_data = {
            "coord": {"lon": -74.006, "lat": 40.7143},
            "weather": [{"main": "Clouds", "description": "scattered clouds"}],
            "main": {"temp": 5, "feels_like": 2, "pressure": 1012, "humidity": 80},
            "wind": {"speed": 3.1, "deg": 250},
            "clouds": {"all": 40},
            "sys": {"country": "US"},
            "name": "New York",
            "cod": 200
        }

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data

        params = {"q": CITY, "appid": API_KEY, "units": UNITS}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        self.assertEqual(response.status_code, 200, "❌ Mock API call failed!")
        self.assertEqual(data["name"], "New York", "❌ City name mismatch!")
        self.assertEqual(data["cod"], 200, "❌ Invalid response code!")


if __name__ == "__main__":
    unittest.main()
