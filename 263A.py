from math import floor

matrix = []

for i in range(5):
    inp = list(map(int, input().split()))
    matrix.append(inp)

# Beautiful Matrix if the 1 is in the third row and third column (index: [2][2])
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row = i
            col = j
            res = floor(abs(2-i) + abs(2-j))
            print(res)
            break
