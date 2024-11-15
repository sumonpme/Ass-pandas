# Example 47: Pandas - Using pd.cut for Binning Data
import pandas as pd

# Sample DataFrame
data = {
    'Age': [23, 35, 45, 50, 60, 62, 70, 80, 90]
}

df = pd.DataFrame(data)

# Defining bin edges
bins = [0, 30, 60, 90]

# Binning the 'Age' column into defined intervals
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=['0-30', '31-60', '61-90'])

print(df)
