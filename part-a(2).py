dist_matrix = []

for i in range(6):
    row = []
    for j in range(6):
        value = (i + 1) + (j + 1)
        row.append(value)
    dist_matrix.append(row)
for row in dist_matrix:
    print(row)
