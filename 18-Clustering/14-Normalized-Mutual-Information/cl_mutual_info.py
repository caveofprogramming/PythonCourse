from sklearn.metrics import normalized_mutual_info_score

y_true = [1, 1, 1, 0, 0, 0]
y_predicted = [0, 0, 0, 1, 1, 1]

print(normalized_mutual_info_score(y_true, y_predicted))