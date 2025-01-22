import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={"326d872ae324fb8620f6c5a5ee5ca7d8"}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    city = input("Enter city: ")
    data = get_weather_data(city, API_KEY)
    if data:
        print(data)
    else:
        print("Failed to fetch data.")
