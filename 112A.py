n1 = input()
n2 = input()

res = 0

if n1.lower() < n2.lower():
    print(-1)
elif n1.lower() > n2.lower():
    print(1)
else:
    print(0)