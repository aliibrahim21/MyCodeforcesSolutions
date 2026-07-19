from math import ceil


n, m, a = tuple(map(int, input().split()))

j = ceil(n / a) * ceil(m / a)

print(j)