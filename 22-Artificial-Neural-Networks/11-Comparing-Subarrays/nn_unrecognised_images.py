import numpy as np

a1 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1], [0, 1, 0]])
a2 = np.array([[0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 0, 1], [1, 0, 0]])

b = [i for i in range(len(a1)) if np.argmax(a1[i]) != np.argmax(a2[i])]

print(b)