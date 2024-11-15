# Example 29: Pandas - Sorting by Multiple Columns
import pandas as pd

data = {
    'student': ['Alif', 'Baki', 'Chandu', 'Dad'],
    'Marks': [800, 920, 700, 900],
    'Grade': ['B', 'A+', 'A-', 'A']
}

df = pd.DataFrame(data)

# Sort by Age (ascending) and Score (descending)
sorted_df = df.sort_values(by=['Marks', 'Grade'], ascending=[True, False])

print("\nDataFrame Sorted by Marks and Grade:")
print(sorted_df)
