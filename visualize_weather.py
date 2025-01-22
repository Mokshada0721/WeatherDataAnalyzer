import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather_data = [
    {"city": "New York", "temperature": 5, "humidity": 80},
    {"city": "London", "temperature": 10, "humidity": 70},
    {"city": "Mumbai", "temperature": 30, "humidity": 60},
    {"city": "Tokyo", "temperature": 15, "humidity": 65}
]

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# Temperature bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x='city', y='temperature', data=df, palette='coolwarm')
plt.title('City vs Temperature')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.show()

# Humidity bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x='city', y='humidity', data=df, palette='viridis')
plt.title('City vs Humidity')
plt.xlabel('City')
plt.ylabel('Humidity (%)')
plt.show()
