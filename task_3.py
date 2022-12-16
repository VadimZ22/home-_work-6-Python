# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

import random

lst = [random.randint(0,10) for _ in range(10)]
print(lst)
res = list(filter(lambda i: lst.count(i) == 1, lst))
print(res)