# Example 27: Pandas - Filtering with isin Method
import pandas as pd

# Sample DataFrame
data = {
    'Student name': ['Akib', 'Rahim', 'Kamal', 'Jamal'],
    'Class': ['ten', 'six', 'eight', 'seven'],
    'Roll': [6, 8, 7, 10]
}

df = pd.DataFrame(data)

# Filter based on multiple classes
filtered_df = df[df['Class'].isin(['ten', 'seven'])]

print(filtered_df)
