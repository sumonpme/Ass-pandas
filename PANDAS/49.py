# Example 49: Pandas - Using DataFrame.eval for Efficient Calculations
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)

# Use eval() )
df['D'] = df.eval('A + B')

print(df)
