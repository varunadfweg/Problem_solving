from collections import Counter

dist_matrix = []

for i in range(6):
    row = []
    for j in range(6):
        value = (i + 1) + (j + 1)
        row.append(value)
    dist_matrix.append(row)

sums = []
for row in dist_matrix:
    for sum_value in row:
        sums.append(sum_value)

sum_counts = Counter(sums)

total_combinations = 6 * 6

probabilities = {}
for sum_value, count in sum_counts.items():
    probabilities[sum_value] = count / total_combinations

for sum_value, probability in probabilities.items():
    print("Sum = {}, Probability = {:.4f}".format(sum_value, probability))
