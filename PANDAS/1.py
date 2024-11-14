# Example 1: Pandas - Grouping and Aggregation
import pandas as pd


# Sample data 
data = {
    'Employee': ['A1', 'B2', 'C3', 'D4', 'E5', 'F6'],
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT', 'IT'],
    'Salary': [50000, 60000, 52000, 58000, 70000, 72000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Department' 
grouped_df = df.groupby('Department').agg({
    'Salary': ['mean', 'sum'],       
    'Employee': 'count'              
})
print("Grouped and Aggregated DataFrame:\n", grouped_df)


