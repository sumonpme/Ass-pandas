# Example 22: Pandas - Creating Dummy Variables
import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Creating dummy variables for the 'Category' column
df_dummies = pd.get_dummies(df, columns=['Category'], drop_first=True)

print(df_dummies)
