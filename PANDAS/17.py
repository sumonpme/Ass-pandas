# Example 17: Pandas - Using map() for Value Replacement
import pandas as pd

# Sample data
data = {
    'Person': ['Alif', 'Baki', 'Chandu', 'David'],
    'position': ['HR', 'MD', 'SALES', 'ACCONTANT']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define a mapping dictionary for positions
position_mapping = {
    'HR': 'Human Resources',
    'MD': 'Managing Director',
    'SALES': 'Salesperson',
    'ACCONTANT': 'Accountant'  
}

# Use map() 
df['position_full'] = df['position'].map(position_mapping)

print(df)


