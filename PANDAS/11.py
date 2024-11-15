# Example 11: Pandas - Rolling Window Calculations
import pandas as pd

# Sample DataFrame with 10 sales values
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Sales': [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
}

df = pd.DataFrame(data)

# Calculate the 3-day moving average
df['3-Day Moving Average'] = df['Sales'].rolling(window=3).mean()

print(df)



