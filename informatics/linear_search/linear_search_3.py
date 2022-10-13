"""
Линейный поиск - 3
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

Напишите программу, которая выводит номера элементов массива, равных данному числу.

Входные данные
В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
Во второй строке вводятся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
В третьей строке содержится одно целое число x, не превосходящее по модулю 1000.

Выходные данные
Вывести номера элементов, равных данному, в порядке возрастания. Если таких элементов нет, ничего выводить не нужно.
"""


def get_indexes_of_equals(array_size: str, array_str: str, number_to_find: str) -> str:
    search_array = [int(number) for number in array_str.split(sep=' ')]
    search_array.append(int(number_to_find))  # has index == <array_size>
    n = int(array_size)
    indexes_list = []
    for i in range(n):
        if search_array[i] == search_array[n]:
            indexes_list.append(str(i + 1))  # add 1 because indexing starts with 0, which doesn't fit task
    return ' '.join(indexes_list)


# print(get_indexes_of_equals(input(), input(), input()))
