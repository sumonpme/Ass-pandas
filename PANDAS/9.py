# Example 9: Pandas - Conditional Filtering with Multiple Conditions
import pandas as pd

# DataFrame
data = {
    'Employee': ['A1', 'B2', 'C3', 'D4', ],
    'Salary': [3000, 5000, 6000, 4000,],
    'Experience': [3, 5, 6, 2 ]
}

df = pd.DataFrame(data)

# Applying multiple conditions
filtered_df = df[(df['Salary'] > 4000) & (df['Experience'] > 3)]

print(filtered_df)
