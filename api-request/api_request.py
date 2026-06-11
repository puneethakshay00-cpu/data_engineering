import requests

api_key = "061c964a5d2a3140851f3e0e6f45824a"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        print("API response received successfully.")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise


