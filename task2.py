# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

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
    print(list)

def mult_couple_elements(lst):
    if len(lst) % 2 != 0:
        length = len(lst)//2 + 1 
    else:
        length = len(lst)//2
    new_lst = []
    for i in range(length):
        new_lst.append(lst[i]*lst[len(lst)-i-1])
        i+=1
    print(new_lst)


get_random_number(n_list, n, x_min, x_max)
mult_couple_elements(n_list)