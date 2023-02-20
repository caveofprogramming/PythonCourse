from itertools import permutations
import numpy as np
from sklearn.metrics import r2_score

def find_best_perm(y_true, y_predicted):
    scores = {}
    for perm in permutations(range(max(y_true) + 1)):
        score = r2_score(y_true, np.choose(y_predicted, perm))
        scores[score] = perm

    max_score = max(scores.keys())
    return scores[max_score]


y_true = [0, 0, 1, 1, 2, 2]
y_predicted = [1, 1, 0, 0, 2, 2]

perm = find_best_perm(y_true, y_predicted)

print(r2_score(y_true, np.choose(y_predicted, perm)))