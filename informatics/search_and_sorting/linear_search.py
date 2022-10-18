def get_saddle_points(rows_count: int, columns_count: int, matrix: list) -> int:
    """
    Return number of saddle points in matrix
    :param rows_count: 1 <= int <= 750
    :param columns_count: 1 <= int <= 750
    :param matrix: list of <rows_count> lists with <columns_count> elements, |element| <= 1000
    :return: int number of saddle points

    Задача Матрица
    Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

    Задана матрица K, содержащая n строк и m столбцов.
    Седловой точкой этой матрицы назовем элемент, который одновременно является минимумом в своей строке и максимумом в своем столбце.
    Найдите количество седловых точек заданной матрицы.

    Входные данные
    Первая строка содержит целые числа n и m (1 ≤ n, m ≤ 750). Далее следуют n строк по m чисел в каждой. j-ое число i-ой строки равно kij.
    Все kij по модулю не превосходят 1000.

    Выходные данные
    Выведите ответ на задачу.
    """
    saddle_points_count = 0

    row_min_list = []
    for i in range(rows_count):
        row_min = 1001
        for j in range(len(matrix[i])):
            if matrix[i][j] < row_min:
                row_min = matrix[i][j]
        for j in range(len(matrix[i])):
            if matrix[i][j] == row_min:
                row_min_list.append((matrix[i][j], i, j))

    columns_max_list = []
    for j in range(columns_count):
        columns_max = -1001
        for i in range(rows_count):
            if matrix[i][j] > columns_max:
                columns_max = matrix[i][j]
        for i in range(rows_count):
            if matrix[i][j] == columns_max:
                columns_max_list.append((matrix[i][j], i, j))
                if (matrix[i][j], i, j) in row_min_list:
                    saddle_points_count += 1

    return saddle_points_count


if __name__ == '__main__':
    n, m = [int(num) for num in input().split(sep=' ')]
    matrix_list = []
    for i in range(n):
        matrix_list.append([int(num) for num in input().split(sep=' ')])
    print(get_saddle_points(n, m, matrix_list))
