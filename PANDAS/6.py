# Example 6: Pandas - Pivoting DataFrames
import pandas as pd

# Sample data
data = {
    'Student name': ['Akib', 'Rahim', 'kamal', 'Jamal'],
    'Class': ['ten', 'six', 'eight', 'seven'],
    'Roll': [6, 8, 7, 10]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
