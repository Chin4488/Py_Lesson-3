# 2.	Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

import math
d = float(input('Введите точность числа Пи: '))
precision = 0
while d < 1:
    precision += 1
    d *= 10
print('{:.{}f}'.format(math.pi, precision))
