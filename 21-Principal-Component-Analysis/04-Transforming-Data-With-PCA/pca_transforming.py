import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

intercept = 40
gradient = 0.5
startx = 0
endx = 200

midx = (endx - startx)/2
midy = intercept + gradient * midx

perpendicular_gradient = -1/gradient
perpendicular_intercept = midy + midx/gradient


limit = 250

x = np.arange(startx, endx, 5)
y = intercept + (gradient * x) + np.random.normal(scale=10, size=len(x))

X = np.append(x.reshape(-1, 1), y.reshape(-1, 1), axis=1)

model = PCA()
components = model.fit_transform(X)

print(components)

fig, axes = plt.subplots(figsize=(16,8), ncols=2)

ax = axes[0]
ax.set_xlim(0, limit)
ax.set_ylim(0, limit)
ax.scatter(midx, midy, s=100, color='red')
ax.plot(x, intercept + gradient * x)
ax.plot(x, perpendicular_intercept + perpendicular_gradient * x)
ax.scatter(x, y, c=x)

ax = axes[1]
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.scatter(components[:,0], components[:,1])

plt.show()