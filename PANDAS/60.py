# Example 60: Pandas - Creating Custom Indexes with MultiIndex
import pandas as pd
data = {
    'Student name': ['Akib', 'Rahim', 'Kamal', 'Akib', 'Jamal', 'Rahim'],
    'Class': ['ten', 'six', 'eight', 'ten', 'seven', 'six'],
    'Roll': [6, 8, 7, 6, 10, 8]
}

df = pd.DataFrame(data)
df.set_index(['Class', 'Roll'], inplace=True)

print(df)