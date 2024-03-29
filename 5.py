import math
import os
os.system('cls')

dir = r'C:\Geekbrains\Python\for Tinkoff\Академия Data Science 2024\product\solutions\programming\5'
os.chdir(dir)

MyFile = open('Input.txt', 'r')
MyFile.seek(0)
n, m = map(int, MyFile.readline().strip().split(' '))
MyFile.close()

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
