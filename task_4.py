# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

lst = [int(i) for i in input("enter elements: ").split()]
print(lst)
res = list(map(lambda i: i*lst[(-lst.index(i)-1)], lst[:round(len(lst)/2 + 0.5)]))
print(res)