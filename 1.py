import os
# Количество слов sheriff

os.system('cls')


def print_s(quantity, mas_s):
    print(quantity)
    mas_s = list(map(str, mas_s))

    zx = (' '.join(mas_s))
    print(zx)


dir = r'C:\Geekbrains\Python\for Tinkoff\Академия Data Science 2024\product\solutions\programming\1'


os.chdir(dir)


MyFile = open('Input.txt', 'r')
MyFile.seek(0)
#Content = MyFile.read().split()
str1 = MyFile.readline()
str2 = MyFile.readline()
MyFile.close()

dict = {}
lens = []
a = (str1.split(' '))
maxl = 0
maxi = 0
a.sort()
for i in range(len(a)):
    #dict[i] = len(i)
    buf = len(a[i])
    if maxl < buf:
        maxl = buf
        maxi = i
print(a[maxi])
print(maxi)
