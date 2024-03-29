import os
os.system('cls')
dir = r'C:\Geekbrains\Python\for Tinkoff\Академия Data Science 2024\product\solutions\programming\2'
os.chdir(dir)

MyFile = open('Input.txt', 'r')
MyFile.seek(0)
a, b, c, d = map(int, MyFile.readline().strip().split(' '))
MyFile.close()

if a == 0 and b == 0:
    print('INF')
elif a == 0 or b * c == a * d:
    print('NO')
elif b % a == 0:
    x = -b // a
    print(x)
else:
    print('NO')
