import numpy as np
import matplotlib.pyplot as plt

intercept = 40
gradient = 0.5
startx = 0
endx = 200

limit = 250

x = np.arange(startx, endx, 5)
y = intercept + (gradient * x) + np.random.normal(scale=10, size=len(x))

fig, ax = plt.subplots(figsize=(8,8))

ax.set_xlim(0, limit)
ax.set_ylim(0, limit)
ax.scatter(x, y, c=x)

plt.show()