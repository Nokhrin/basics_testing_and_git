"""
Ревизия
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

В связи с визитом Императора Палпатина было решено обновить состав дроидов в ангаре 32. Из-за кризиса было решено новых дроидов не закупать, но выкинуть пару старых. Как известно, Палпатин не переносит дроидов с маленькими серийными номерами, так что все, что требуется - найти среди них двух, у которых серийные номера наименьшие.

Входные данные
Первая строка входного файла содержит целое число N – количество дроидов. (2 ≤ N ≤ 1000), вторая строка – N целых чисел, по модулю не превышающих 2*(10^9) – номера дроидов

Выходные данные
Выведите два числа: первым – последний по величине из номеров дроидов (такого следует утилизировать в первую очередь), а вторым – предпоследний.
"""


def get_two_min_values(numbers_count: str, numbers_input: str) -> str:
    """Return min value from list and number next by value as string of two numbers, separated by space"""
    total_numbers = int(numbers_count)
    numbers_list = [int(number) for number in numbers_input.split(sep=' ')]
    min_values = []
    while len(min_values) < 2:
        current_min = 2 * (10 ** 9) + 1
        for i in range(total_numbers):
            if numbers_list[i] < current_min and str(numbers_list[i]) not in min_values:
                current_min = numbers_list[i]
        min_values.append(str(current_min))
    return ' '.join(min_values)


# print(get_two_min_values(input(), input()))
