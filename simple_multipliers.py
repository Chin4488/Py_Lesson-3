# 3.	Составить список простых множителей натурального числа n

number = int(input('Введите натуральное число: '))
list = []
i = 2
while i * i <= number:
    while number % i == 0:
        list.append(i)
        number = number / i
    i = i + 1
if number > 1:
    list.append(int(number))
print(list)