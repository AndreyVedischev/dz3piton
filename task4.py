# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))

def conversion_to_binary(n):
    bin = ""
    while n > 0:
        bin = str(n % 2) + bin
        n = n // 2
    print(bin)

conversion_to_binary(number)