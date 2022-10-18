"""
Приближенный двоичный поиск
Реализуйте алгоритм приближенного бинарного поиска.

Входные данные
В первой строке входных данных содержатся числа N и K (0<N,K<100001).
Во второй строке задаются N чисел первого массива, отсортированного по неубыванию,
в третьей строке – K чисел второго массива.
Каждое число в обоих массивах по модулю не превосходит 2⋅10^9


Выходные данные
Для каждого из K чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному.
Если таких несколько, выведите меньшее из них.
"""


def do_approximate_binary_search(list_one_len: int, list_two_len: int, list_one: list, list_two: list) -> str:
    """For each number in list_two number return the closest number from list_one"""

    return '1'


if __name__ == '__main__':
    N, K = [int(num) for num in input().split(sep=' ')]
    list_1 = [int(num) for num in input().split(sep=' ')]
    list_2 = [int(num) for num in input().split(sep=' ')]
    do_approximate_binary_search(N, K, list_1, list_2)

"""
Примеры
Входные данные

5 5
1 3 5 7 9 
2 4 8 1 6 

Выходные данные

1
3
7
1
5
"""
