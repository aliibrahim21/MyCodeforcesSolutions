import math


m, n = tuple(map(int, input().split()))

mxn = m * n

res = math.floor(mxn / 2)

print(res)