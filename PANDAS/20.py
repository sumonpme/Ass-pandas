# Example 20: Pandas - Using Rank to Rank Values
import pandas as pd
# Sample data
data = {
    'Person': ['Alif', 'Baki', 'Chandu', 'David'],
    'Salary': [8000, 9000, 10000, 7000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Rank the scores 
df['Rank'] = df['Salary'].rank()
print('DataFrame with Ranked Scores:\n', df)