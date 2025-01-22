from fetch_weather import get_weather_data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "your_api_key_here"

def visualize_data(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x='city', y='temperature', data=df, palette='coolwarm')
    plt.title('City vs Temperature')
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.barplot(x='city', y='humidity', data=df, palette='viridis')
    plt.title('City vs Humidity')
    plt.show()

def main():
    cities = ["New York", "London", "Mumbai", "Tokyo"]
    weather_data = []

    for city in cities:
        data = get_weather_data(city, API_KEY)
        if data:
            weather_data.append({
                "city": city,
                "temperature": data['main']['temp'],
                "humidity": data['main']['humidity']
            })

    df = pd.DataFrame(weather_data)
    print(df.describe())
    visualize_data(df)

if __name__ == "__main__":
    main()
