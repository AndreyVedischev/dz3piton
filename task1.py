# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

n = int(input('Введите число элементов списка: '))
x_min = int(input('Введите диапазон min: '))
x_max = int(input('Введите диапазон max: '))

n_list = []

def get_random_number(list, len, min, max):
    rnd = randint    
    for i in range(0, len):
        number = rnd(min, max)
        list.append(number)
    return(list)

def sum_odd_elements(list,len):
    sum = 0
    for i in range(1,len,2):
        sum += list[i]
    return sum

print(get_random_number(n_list, n, x_min, x_max))
print(sum_odd_elements(n_list, n))