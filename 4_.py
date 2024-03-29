import os
os.system('cls')


n, l = map(int, input().strip().split(' '))
b = list(map(int, input().strip().split(' ')))
b.sort()


summ = 0
i = 0
while i < len(b):
    if b[i]+l >= b[i+1]:
        summ += 1
        i += 2
    else:
        summ += 1
        i += 1
print(summ)
