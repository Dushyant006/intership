import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

print("🔄 Step 2: Loading historical data...")
# 1. Read the CSV file we generated in Step 1
df = pd.read_csv('historical_cloud_costs.csv')

# Convert the log_date column into actual datetime objects so Python understands time
df['log_date'] = pd.to_datetime(df['log_date'])

# 2. Prepare data for Machine Learning
# AI models don't understand dates like "2026-05-28", they need numbers.
# We will create a column called 'day_number' (Day 1, Day 2, Day 3...)
start_date = df['log_date'].min()
df['day_number'] = (df['log_date'] - start_date).dt.days

# X = What the model learns from (Day Numbers)
# y = What the model is trying to predict (Daily Costs)
X = df[['day_number']]
y = df['daily_cost']

print("🤖 Training the AI model to recognize cost trends...")
# 3. Train the Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Calculate model accuracy (R² Score)
accuracy = model.score(X, y)
print(f"📈 Model Training Complete. Trend accuracy score: {accuracy:.2f}")

print("🔮 Forecasting the next 30 days of cloud expenses...")
# 4. Generate the next 30 future days
last_day_number = df['day_number'].max()
last_date = df['log_date'].max()

future_data = []
for i in range(1, 31):  # 30 days into the future
    future_day = last_day_number + i
    future_date = last_date + timedelta(days=i)
    
    # Let the AI predict the cost for this future day number
    # (Using a clean dictionary format to avoid layout warnings)
    predicted_cost = model.predict(pd.DataFrame({'day_number': [future_day]}))[0]
    
    # To keep it ultra-realistic, let's inject a weekend drop pattern into predictions
    if future_date.weekday() >= 5:
        predicted_cost -= 25.0  # Weekend discount trend
        
    future_data.append([
        future_date.strftime('%Y-%m-%d'),
        'AWS Cloud Infrastructure',
        'Engineering',
        round(predicted_cost, 2),
        24 # Expected full usage hours
    ])

# 5. Save the predictions to a brand new CSV file
df_forecast = pd.DataFrame(future_data, columns=['log_date', 'service_name', 'department', 'daily_cost', 'usage_hours'])
df_forecast.to_csv('predicted_cloud_costs.csv', index=False)

print("\n🎉 SUCCESS! 'predicted_cloud_costs.csv' has been created.")
print("-" * 60)
print("👀 PREVIEW OF YOUR FUTURE AI FORECAST (NEXT 30 DAYS):")
print("-" * 60)
print(df_forecast.head(10))
print("-" * 60)