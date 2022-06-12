# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

import os
from random import randint 

def generation_numbers(n):
    max_number = int(input('Введите максимальное число в списке: '))
    with open('numbers.txt', 'w+') as file:
        for _ in range(n):
            file.write(f'{str(randint(1,max_number))} ')

quantity_numbers = int(input('Сколько чисел должно быть в создаваемом файле?: '))
generation_numbers(quantity_numbers)

with open('numbers.txt', 'r') as file:
    read_file = file.read()
print('Введённый список: ', read_file)

file=open("temp.txt", "w")
with open("numbers.txt", "r") as fi:
    for stri in fi:
        if len(stri)>0:
            arr=stri.split()
            tmp=""
            for s in arr:
                if int(s)%2 != 0:
                    tmp+=s+" "
            file.write(tmp+"\n")
        else:
            file.write("\n")
file.close()
os.remove('numbers.txt')
os.rename('temp.txt', 'numbers.txt')
with open('numbers.txt', 'r') as file:
    read_file = file.read()
print('Новый список: ', read_file)