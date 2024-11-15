# Example 15: Pandas - Handling Outliers
import pandas as pd
import numpy as np

# Sample DataFrame 
data = {
    'A': [10, 12, 14, 15, 14, 100 ],
    'B': [100, 105, 98, 120, 115, 130],
    'C': [1, 2, 1, 3, 2, 3]  
}

df = pd.DataFrame(data)
def find_outliers_iqr(df):
    outliers = pd.DataFrame()
    for column in df.select_dtypes(include=['float64', 'int64']):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        outliers[column] = ~((df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR))
    return outliers

outliers_iqr = find_outliers_iqr(df)
print("Outliers based on IQR:\n", outliers_iqr)
