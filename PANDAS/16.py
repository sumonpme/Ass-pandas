# Example 16: Pandas - Creating a Pivot Table with Multiple Aggregations
import pandas as pd
data = {
    'Student name': ['Akib', 'Rahim', 'Kamal', 'Jamal', 'Akib', 'Rahim', 'Kamal', 'Jamal'],
    'Class': ['ten', 'six', 'eight', 'seven', 'ten', 'six', 'eight', 'seven'],
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'Science'],
    'Marks': [85, 78, 88, 90, 82, 75, 80, 89],
    'Attendance': [90, 85, 88, 92, 88, 80, 84, 91]
}
df = pd.DataFrame(data)
pivot_table = pd.pivot_table(
    df,
    index='Student name',                
    columns='Subject',                   
    values=['Marks', 'Attendance'],      
    aggfunc={'Marks': ['mean', 'max'],   
             'Attendance': 'mean'}       
)

print("\nPivot Table with Multiple Aggregations:")
print(pivot_table)