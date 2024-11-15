# Example 26: Pandas - DataFrame Info and Memory Usage
import pandas as pd
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10.5, 20.5, 30.5, 40.5, 50.5],
    'C': ['foo', 'bar', 'baz', 'qux', 'quux'],
    'D': [True, False, True, False, True]
}

df = pd.DataFrame(data)
print(df.memory_usage(deep=True))