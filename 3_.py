import os

os.system('cls')


a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))

if set(a) == set(b):
    print('YES')
else:
    print('NO')
