n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))
res = 0

for i in range(len(a)):
    if a[i] >= a[k-1] and a[i] > 0:
        res = res + 1

print(res)