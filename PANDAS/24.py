# Example 24: Pandas - Assign Method for Adding Columns
import pandas as pd
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Price': [100, 150, 200, 250]
}

df = pd.DataFrame(data)

# Adding a new column 'Discounted Price' by applying a 50% discount
df = df.assign(Discounted_Price = df['Price'] * 0.5)
print(df)