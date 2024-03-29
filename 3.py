import os
# Количество слов sheriff

os.system('cls')


dir = r'C:\Geekbrains\Python\for Tinkoff\Академия Data Science 2024\product\solutions\programming\3'

os.chdir(dir)


MyFile = open('Input.txt', 'r')
MyFile.seek(0)
# Content = MyFile.read().split()
# a_str = MyFile.readline()
# b_str = MyFile.readline().split(' ')
#t = MyFile.readline().rstrip('\n').split(' ')
#t = MyFile.readline().strip().split(' ')

#a = list(map(int, t))
n, l = map(int, MyFile.readline().strip().split(' '))
b = list(map(int, MyFile.readline().strip().split(' ')))
MyFile.close()

if set(a) == set(b):
    print('YES')
else:
    print('NO')
