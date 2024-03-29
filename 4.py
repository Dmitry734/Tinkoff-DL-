import os
os.system('cls')
dir = r'C:\Geekbrains\Python\for Tinkoff\Академия Data Science 2024\product\solutions\programming\4'
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
b.sort()
MyFile.close()

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
