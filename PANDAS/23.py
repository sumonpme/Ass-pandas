# Example 23: Pandas - Query Method for Conditional Filtering
import pandas as pd

# Sample DataFrame
data = {
    'Student name': ['Akib', 'Rahim', 'kamal', 'Jamal'],
    'Class': ['ten', 'six', 'eight', 'seven'],
    'Roll': [6, 8, 7, 10]
}

df = pd.DataFrame(data)

# Using the query method for conditional filtering based on 'Roll' column
filtered_df = df.query('Roll > 7')

print(filtered_df)

