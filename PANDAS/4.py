# Example 4: Pandas - Merging DataFrames with Different Keys
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
# Merging with different keys
merged_df = pd.merge(df1, df2, left_on='Student name', right_on='Class', how='outer')
print('Merged DataFrame:\n', merged_df)