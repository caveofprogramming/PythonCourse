import numpy as np


values = np.arange(10, 101, 10)
rank = np.arange(1, len(values) + 1)

values = 1.0/values

print(values)
print(rank)



for r, v in zip(rank, values):
    print(r/v)