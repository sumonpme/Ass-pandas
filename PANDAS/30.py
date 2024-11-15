# Example 30: Pandas - Using style for DataFrame Styling
import pandas as pd

# Sample DataFrame
data = {
    'student': ['Alif', 'Baki', 'Chandu', 'Dad'],
    'Marks': [800, 920, 700, 900],
    'Grade': ['B', 'A+', 'A-', 'A']
}

df = pd.DataFrame(data)

# Apply style to highlight the maximum marks
styled_df = df.style.highlight_max(subset=['Marks'], color='yellow')

# Option 1: If in Jupyter Notebook
styled_df  

# Option 2: Save to an HTML file for viewing
styled_df.to_html("styled_dataframe.html")
