
"""
ID  Weight  Height
1   70      160
2   60      155
3   100     180
"""

import pandas as pd

df = pd.read_clipboard(index_col=0)

print(df)

height = df['Height']

print(type(height))
print(height)

print(type(height.index))
print(list(height.index))
print()
print(type(height.values))
print(list(height.values))

print()
print(height.mean())
