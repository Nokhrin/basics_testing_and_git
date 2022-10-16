"""
Ближайшее число
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

Напишите программу, которая находит в массиве элемент, самый близкий по величине к  данному числу.

Входные данные
В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.

Выходные данные
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.
"""


def get_nearest_number(array_size: str, array_str: str, number_to_find: str) -> int:
    numbers = [int(number) for number in array_str.split(sep=' ')]
    numbers.append(int(number_to_find))
    n = int(array_size)
    min_diff = 2001  # possible values are between -1000 and 1000, max difference is 2000
    index_min = -1
    for i in range(n):
        if abs(numbers[i] - numbers[n]) < min_diff:
            min_diff = abs(numbers[i] - numbers[n])
            index_min = i
    return numbers[index_min]


if __name__ == '__main__':
    print(get_nearest_number(input(), input(), input()))  # for examination purposes
