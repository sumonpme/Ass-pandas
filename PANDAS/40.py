# Example 40: Pandas - Using drop_duplicates() for Unique Rows
import pandas as pd
data = {
    'Student name': ['Akib', 'Rahim', 'Kamal', 'Akib', 'Jamal', 'Rahim'],
    'Class': ['ten', 'six', 'eight', 'ten', 'seven', 'six'],
    'Roll': [6, 8, 7, 6, 10, 8]
}

df = pd.DataFrame(data)

# Remove duplicate rows based on all columns
df_unique = df.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(df_unique)