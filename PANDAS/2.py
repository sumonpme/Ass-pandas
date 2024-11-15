# Example 2: Pandas - MultiIndex DataFrame Operations
import pandas as pd
import pandas as pd

# Create MultiIndex
arrays = [
    ['A', 'B', 'C', 'D'],
    ['20', '21', '22', '23']
]
index = pd.MultiIndex.from_arrays(arrays, names=('STUDENT', 'ROLL'))

# Create DataFrame
data = {
    'Marks': [800, 750, 600, 850],
    'Position': [3, 5, 7, 2]
}
df = pd.DataFrame(data, index=index)

print("MultiIndex DataFrame:")
print(df)
