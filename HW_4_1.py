#1. Написать программу которая будет проверять четность некоторого числа.

import math
a=int(input("Input A:"))
b = int (a % 2)
# print (b)
if b==1:
    print ('нечетное число')
else:
    print('четное число')
