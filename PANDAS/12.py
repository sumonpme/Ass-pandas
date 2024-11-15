# Example 12: Pandas - Shift and Lagging Data
import pandas as pd

# Sample data
data = {
    'Student name': ['Akib', 'Rahim', 'Kamal'],
    'Class': ['ten', 'six', 'eight'],
}

# Create DataFrame
df = pd.DataFrame(data)

# Shift the "Class" column down by 1 period (lagging)
df['Class_Lagged'] = df['Class'].shift(1)

print(df)
