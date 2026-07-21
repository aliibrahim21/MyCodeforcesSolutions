s = list(map(int, input().split('+')))

for i in range(len(s)):
    swapped = False
    for j in range(len(s) - 1 - i):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
            swapped = True
    if not swapped:
        break

for k in range(len(s)):
    if k == len(s) - 1:
        print(f'{s[k]}', end='')
    else:
        print(f'{s[k]}+', end='')
print()