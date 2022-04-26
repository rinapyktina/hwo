matrix = [2, 4, 6, 7, 3, 4, 6, 7]
print(len(set(matrix)))
for i in set(matrix):
    print(i)
    count = 0
    for j in matrix:
        if i == j:
            count += 1
    print("Входит:", count)