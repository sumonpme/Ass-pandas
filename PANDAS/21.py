# Example 21: Pandas - Using applymap for Element-wise Operations
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Using applymap() 
df_squared = df.applymap(lambda x: x ** 2)

print(df_squared)
