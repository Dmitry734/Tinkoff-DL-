import math


n, m = map(int, input().strip().split(' '))

Nod = math.lcm(n, m)

if n > m:
    steps = int((Nod/m-1) % 2)
    ugol = [0, 2, 3]
    answ = ugol[steps]
elif m > n:
    steps = int((Nod/n-1) % 2)
    ugol = [0, 3, 2]
    answ = ugol[steps]
elif m == n:
    answ = 4

print(answ)
