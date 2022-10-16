"""
Дана таблица N × N, заполненная целыми числами. Петр Первый считает столбец хорошим, если тот содержит число Х. Требуется для каждого столбца выяснить, является ли тот хорошим.

Входные данные
В первой строке число X, не превышающее по модулю 2*(10^9). Во второй строке число N (1 <= N <= 100),
В следующих N строках по N целых чисел, не превышающих по модулю 2*(10^9) – числа в ячейках таблицы.

Выходные данные
Для каждого столбца выведите YES, если в нем есть число Х, и NO в противном случае. (Каждый ответ с новой строки)
"""


def get_input():
    """Collect and convert user input"""
    number_to_find = int(input())
    total_rows = int(input())
    rows = [[int(number) for number in input().split(sep=' ')] for i in range(total_rows)]
    return number_to_find, total_rows, rows


def transpose_matrix(matrix_input: list) -> list:
    """
    Return transposed matrix
    Suppose that input is always correct and not empty
    """
    rows_count = len(matrix_input)
    columns_count = len(matrix_input[0])
    # template for transposed matrix
    trans_matrix = [[0 for j in range(columns_count)] for i in range(rows_count)]
    for i in range(rows_count):
        for j in range(columns_count):
            trans_matrix[j][i] = matrix_input[i][j]
    return trans_matrix


def is_number_in_column(number_search: int, rows_count: int, matrix: list) -> str:
    """Return YES (number is in column) or NO for each column"""
    # template for answer
    result_list = ['NO' for i in range(rows_count)]
    trans_matrix = transpose_matrix(matrix)
    rows = len(trans_matrix)
    columns = len(trans_matrix[0])
    for row_index in range(rows):
        for column_index in range(columns):
            if trans_matrix[row_index][column_index] == number_search:
                result_list[row_index] = 'YES'
                break  # leave row on first match
    return '\n'.join(result_list)


if __name__ == '__main__':
    n, count, rows_in = get_input()
    # print(is_number_in_column(n, count, rows_in), end='')
    is_number_in_column(n, count, rows_in)
