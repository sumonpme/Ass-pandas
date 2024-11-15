# Example 7: Pandas - Melting DataFrames
import pandas as pd
import pandas as pd

# Original data
data = {
    'Year': [2020, 2021, 2022],
    'Product_A': [100, 150, 200],
    'Product_B': [80, 120, 160]
}
df = pd.DataFrame(data)

# Adding a Region column
df['Region'] = ['North', 'South', 'East']

# Melt the DataFrame
df_melted = pd.melt(df, id_vars=['Year', 'Region'], var_name='Product', value_name='Sales')

print(df_melted)
