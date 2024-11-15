# Example 14: Pandas - Merging on Multiple Columns
import pandas as pd

# DataFrame 1
data1 = {
    'Student name': ['Akib', 'Rahim', 'kamal'],
    'Class': ['ten', 'six', 'eight'],
    'Roll': [6, 8, 7]
}

df1 = pd.DataFrame(data1)

# DataFrame 2
data2 = {
    'Student name': ['Akib', 'Rahim', 'kamruzz'],
    'Class': ['ten', 'six', 'nine'],
    'Roll': [16, 28, 37]
}
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df1, df2, on=['Student name', 'Class'], how='inner')

print("Merged DataFrame (Inner Join):")
print(merged_df)
