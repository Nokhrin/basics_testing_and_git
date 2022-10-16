"""
Максимальный элемент массива
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

Напишите программу, которая находит значение максимального элемента массива.

Входные данные
В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
Во второй строке вводятся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

Выходные данные
Вывести одно число – значение максимального элемента в массиве.
"""


def get_max_number(array_size: str, array_str: str) -> int:
    search_array = [int(number) for number in array_str.split(sep=' ')]
    n = int(array_size)
    max_num = (-1001, -1)  # number and it's index, from definition, there won't be less than -1000 in input
    for i in range(n):
        if search_array[i] > max_num[0]:
            max_num = (search_array[i], i + 1)  # by definition, indexes start from 1
    return max_num[0]


if __name__ == '__main__':
    print(get_max_number(input(), input()))
