n = int(input())

l = []

for i in range(n):
    j = list(map(int, input().split(' ')))
    l.append(j)

res = 0

for k in l:
    if sum(k) >= 2:
        res = res + 1

print(res)