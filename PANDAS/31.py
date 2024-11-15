# Example 31: Pandas - Using explode() for Nested JSON Columns
import pandas as pd
data = {
    'Student name': ['Akib', 'Rahim', 'Kamal'],
    'Subjects': [['Math', 'Science', 'English'], ['History', 'Geography'], ['Physics', 'Chemistry']]
}

df = pd.DataFrame(data)

# Use explode to split the 'Subjects' 
exploded_df = df.explode('Subjects')

print(exploded_df)