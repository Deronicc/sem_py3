""" Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5 """

import random
import math

n = int(input("Введите кол-во элементом в массиве: "))
x = int(input("Введите число: "))
 

# list=[1,2,3,4,5]
# list = [5,4,3,2,1]
list=[]
for i in range(n):
    list.append(random.randint(1,10))
print(list)

a = math.fabs(list[0]-x)
b = 0

for element in list:
    temp = math.fabs(element - x)
    if temp <= a:
        a = temp
        b = element
    # print(temp, a, b)
print(b)