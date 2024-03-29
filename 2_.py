import os
os.system('cls')

#a, b, c, d = map(int, input().strip().split(' '))
a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
d = int(input().strip())

if a == 0 and b == 0:
    print('INF')
elif a == 0 or b * c == a * d:
    print('NO')
elif b % a == 0:
    x = -b // a
    print(x)
else:
    print('NO')
