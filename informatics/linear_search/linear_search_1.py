"""
Линейный поиск - 1
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

Напишите программу, которая определяет, сколько раз встречается заданное число x в данном массиве.
Входные данные

В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.

Во второй строке вводятся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

В третьей строке содержится одно целое число x , не превосходящее по модулю 1000.
Выходные данные

Вывести одно число – сколько раз встречается x в данном массиве.

"""


def count_appearances(array_size: str, array_str: str, number_search: str) -> int:
    search_array = [int(number) for number in array_str.split(sep=' ')]
    counter = 0
    for i in range(len(search_array)):
        counter += int(search_array[i] == int(number_search))
    return counter


if __name__ == '__main__':
    print(count_appearances(input(), input(), input()))
