# Example 3: Pandas - Using Apply with Lambda Functions
import pandas as pd

# DataFrame
data = {
    'Employee': ['A1', 'B2', 'C3', 'D4'],
    'Salary': [2000, 5000, 7000, 8000]
}

df = pd.DataFrame(data)

# application lambda 
df['Increased salary'] = df['Salary'].apply(lambda x: x *1.2)

print(df)
