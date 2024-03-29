import os

os.system('cls')


a = input().split(' ')


maxl = 0
maxi = 0

for i in range(len(a)):

    buf = len(a[i])
    if maxl < buf:
        maxl = buf
        maxi = i
print(a[maxi])
print(maxl)
