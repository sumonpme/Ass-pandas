# Example 18: Pandas - Detecting Duplicates
import pandas as pd
data = {
    'Name': ['A1', 'B2', 'C3', 'D4',],
    'Age': [25, 30, 35, 25,],
}
# Create a DataFrame
df = pd.DataFrame(data)

# Detect duplicates
duplicates = df.duplicated()
print("Duplicates:" ,duplicates)