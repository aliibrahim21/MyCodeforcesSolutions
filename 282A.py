n = int(input())
X = 0

for i in range(n):
    m = input()

    for x in m:
        if x == "+":
            X = X + 1
            break
        if x == "-":
            X = X - 1
            break

print(X)