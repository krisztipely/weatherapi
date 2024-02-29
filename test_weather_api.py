import os
import requests

def get_weather(api_key, city):
    base_url = "https://api.example.com/weather"
    params = {
        'api_key': api_key,
        'city': city
    }

    response = requests.get(base_url, params=params)

    return response

def test_get_weather():
    api_key = os.getenv('WEATHER_API_KEY')
    if api_key is None:
        raise ValueError("WEATHER_API_KEY environment variable is not set.")

    city = 'New York'

    response = get_weather(api_key, city)

    # Check if the request was successful (status code 200)
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    # Check if the response contains necessary information
    data = response.json()
    assert 'temperature' in data, "Temperature information not found in the response"
    assert 'description' in data, "Weather description not found in the response"

def test_another_city():
    api_key = os.getenv('WEATHER_API_KEY')
    if api_key is None:
        raise ValueError("WEATHER_API_KEY environment variable is not set.")

    city = 'Los Angeles'

    response = get_weather(api_key, city)

    # Check if the request was successful (status code 200)
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    # Check if the response contains necessary information
    data = response.json()
    assert 'temperature' in data, "Temperature information not found in the response"
    assert 'description' in data, "Weather description not found in the response"
