import pandas as pd

# Example data
weather_data = [
    {"city": "New York", "temperature": 5, "humidity": 80},
    {"city": "London", "temperature": 10, "humidity": 70},
    {"city": "Mumbai", "temperature": 30, "humidity": 60},
    {"city": "Tokyo", "temperature": 15, "humidity": 65}
]

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# Analyze
print("Basic Statistics:")
print(df.describe())

print("\nAverage Temperature:")
print(df['temperature'].mean())
