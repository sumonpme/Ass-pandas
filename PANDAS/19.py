# Example 19: Pandas - Using Explode for Lists in Columns
import pandas as pd

data = {
    'Student': ['A1', 'B2', 'C3', 'D4'],
    'Grade': [[80, 85], [90, 92], [95], [98, 99]]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Use explode on the 'Grade' column
df_exploded = df.explode('Grade')

print("DataFrame after Exploding 'Grade' Lists:\n", df_exploded)
