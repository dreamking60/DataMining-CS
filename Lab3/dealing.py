import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, np.nan, 8],
                   'C': [9, 10, 11, 12]})

# Check if each column contains at least one missing value
print(df)
missing_cols = df.isna().any(axis=0)
print(missing_cols)

# Check if each row contains at least one missing value
missing_rows = df.isna().any(axis=1)
print(missing_rows.values)
print(missing_rows)

print(df[[False,True,True,False]])
print(df.loc[:, [True,True,False]])