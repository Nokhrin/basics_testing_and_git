"""
Линейный поиск - 2
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

Напишите программу, которая определяет, встречается ли заданное число x в данном массиве.
Входные данные

В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.

Во второй строке вводятся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

В третьей строке содержится одно целое число x, не превосходящее по модулю 1000.
Выходные данные

Вывести YES , если число x встречается в данном массиве, и NO в противном случае.
"""


def is_in_array(array_size: str, array_str: str, number_to_find: str) -> str:
    search_array = [int(number) for number in array_str.split(sep=' ')]
    search_array.append(int(number_to_find))  # has index == <array_size>
    n = int(array_size)
    for i in range(n):
        if search_array[i] == search_array[n]:
            return 'YES'
    return 'NO'


# print(is_in_array(input(), input(), input()))
