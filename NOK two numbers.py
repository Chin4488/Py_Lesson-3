# 1.	Найти НОК двух чисел.

def nok_two_numbers(a, b):
    if a > b:
        temp = a
    else:
        temp = b
    while(True):
        if ((temp % a == 0) and (temp % b == 0)):
            nok = temp
            break
        temp += 1
    return nok

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print('НОК =', nok_two_numbers(num1, num2))