# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


a_list = [1.1, 1.2, 3.1, 5, 10.01]

def difference_elements(lst):
    lst = []
    for i in a_list:
        if i %1 != 0:
            lst.append(round(i%1,2))
    print(max(lst)-min(lst))


difference_elements(a_list)