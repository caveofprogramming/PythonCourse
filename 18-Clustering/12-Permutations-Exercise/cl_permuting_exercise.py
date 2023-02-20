from itertools import permutations
import numpy as np

y_true = [0, 0, 1, 1, 2, 2]
y_predicted = [1, 1, 0, 0, 2, 2]

for perm in permutations([0, 1, 2]):
    print(perm)

print(np.choose(y_predicted, ['zero', 'one', 'two']))