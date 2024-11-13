# Example 13: Pandas - Cumulative Sum and Product
import pandas as pd

# DataFrame
data = {
    'Students': ['A1', 'B2', 'C3', 'C4'],
    'CGPA': [3.5, 3.0, 3.2, 3.3]
}

df = pd.DataFrame(data)

# cumulative sum
df['Cumulative Sum'] = df['CGPA'].cumsum()

# cumulative product
df['Cumulative Product'] = df['CGPA'].cumprod()

print(df)
