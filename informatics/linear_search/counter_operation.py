"""
Контроперация
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот (все максимальные - на минимальные).

Входные данные
Дано количество оценок Василия (не больше 100), затем сами оценки.

Выходные данные
Требуется вывести исправленные оценки в том же порядке.
"""
import sys


def replace_max_with_min(marks: str) -> str:
    """Return numbers with max replaced by min value"""
    tmp_list = [int(mark) for mark in marks.split(sep=' ')]
    marks_count = tmp_list[0]

    if marks_count < 1:
        return ''

    marks_list = tmp_list[1:]

    max_value = -1
    min_value = 6

    for i in range(marks_count):
        if marks_list[i] > max_value:
            max_value = marks_list[i]
        if marks_list[i] < min_value:
            min_value = marks_list[i]

    max_values_indexes = []
    for i in range(marks_count):
        if marks_list[i] == max_value:
            max_values_indexes.append(i)

    for max_index in max_values_indexes:
        marks_list[max_index] = min_value

    return ' '.join([str(num) for num in marks_list])


if __name__ == '__main__':
    print(replace_max_with_min(input()))
