# Example 10: Pandas - Creating Custom Categorical Data
import pandas as pd
data = ['low', 'medium', 'high', 'medium', 'low', 'high', 'medium', 'low']

categories = ['low', 'medium', 'high']

cat_series = pd.Categorical(data, categories=categories, ordered=True)
df = pd.DataFrame({'Priority': cat_series})

print(df)
print("\nCategory details:")
