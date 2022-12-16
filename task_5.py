# Доделать:
# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;
#     6 + ( 2 * ( 8 - 3 ) / 5 ) - 4 => 2



# Программа работает для одинарных и двойных скобок, но пока только для одних ))))



def get_slice(lst):
    if '(' not in lst:
        return get_result(lst)
    else:
        for i in range(len(lst)):
            if lst[i] == '(': start = i
            if lst[-i - 1] == ')':
                end = -i - 1
            else:
                continue
        slice = lst[start + 1:end]
        print(slice)
        lst = lst[:start + 1] + lst[end + 1:]
        print(lst)
        lst[start] = str(get_slice(slice)[0])
        print(lst[start])
        print(lst)
        return get_slice(lst)


def get_result(lst):
    while len(lst) != 1:
        while '*' in lst or '/' in lst:
            try: div_index = lst.index('/')
            except: div_index = 100

            try: prod_index = lst.index('*')
            except: prod_index = 100

            if prod_index < div_index:
                lst[prod_index - 1] = float(lst[prod_index - 1]) * float(lst[prod_index + 1])
                lst.pop(prod_index + 1)
                lst.pop(prod_index)
            else:
                lst[div_index - 1] = float(lst[div_index - 1]) / float(lst[div_index + 1])
                lst.pop(div_index + 1)
                lst.pop(div_index)

        while '+' in lst or '-' in lst:
            try: sum_index = lst.index('+')
            except: sum_index = 100

            try: deg_index = lst.index('-')
            except: deg_index = 100
            if sum_index < deg_index:
                lst[sum_index - 1] = float(lst[sum_index - 1]) + float(lst[sum_index + 1])
                lst.pop(sum_index + 1)
                lst.pop(sum_index)
            else:
                lst[deg_index - 1] = float(lst[deg_index - 1]) - float(lst[deg_index + 1])
                lst.pop(deg_index + 1)
                lst.pop(deg_index)
        return lst



lst = input('введите выражение: ').split()
print(get_slice(lst))

