import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)

n, bins, patches = plt.hist(x, bins=[-5, -1, 1, 5], edgecolor='white')

print(n, bins, patches)

for patch in patches:
    print(patch)

plt.show()