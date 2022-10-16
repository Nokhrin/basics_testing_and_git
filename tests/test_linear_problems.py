import pytest
from informatics.linear_search.auditing import get_two_min_values
from informatics.linear_search.columns import is_number_in_column
from informatics.linear_search.counter_operation import replace_max_with_min
from informatics.linear_search.linear_search_2 import is_in_array
from informatics.linear_search.linear_search_3 import get_indexes_of_equals
from informatics.linear_search.max_number_in_array import get_max_number
from informatics.linear_search.max_number_index_in_array import get_max_number_index
from informatics.linear_search.nearest_number import get_nearest_number
from informatics.linear_search.silver_medal import get_second_max


class TestLinearProblems:
    @pytest.mark.parametrize(
        argnames='numbers_amount, numbers_array, expected',
        argvalues=[
            ('5', '10 2 3 1 5', '1 2'),
        ]
    )
    def test_get_two_min_values(self, numbers_amount, numbers_array, expected):
        """Test output of get_two_min_values"""
        assert expected == get_two_min_values(numbers_amount, numbers_array)

    @pytest.mark.parametrize(
        argnames='actual_num, actual_rows, actual_matrix, expected_output',
        argvalues=[
            (1789, 1, [[1789]], "YES"),
            (9, 1, [[1789]], "NO"),
            (5, 2, [[4, 5], [2, 3]], "NO\nYES"),
            (5, 2, [[0, 0], [0, 0]], "NO\nNO"),
            (5, 2, [[5, 5], [0, 5]], "YES\nYES"),
            (5, 3, [[5, 6, 7], [1, 2, 3], [-9, -1231, 33]], "YES\nNO\nNO"),
            (-6, 4, [[-5, -6, -7, 9],
                     [-1, -2, -6, 4],
                     [-6, -1231, 33, 44],
                     [-6, -1231, 33, -6]], "YES\nYES\nYES\nYES"),
        ]
    )
    def test_is_number_in_column(self, actual_num, actual_rows, actual_matrix, expected_output):
        """Test output"""
        assert is_number_in_column(actual_num, actual_rows, actual_matrix) == expected_output

    @pytest.mark.parametrize(
        argnames='test_marks, expected_result',
        argvalues=[
            ('5 1 3 3 3 4', '1 3 3 3 1'),
            ('100 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5 5 4 2 2 4 5 4 2 2 5', '2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2 2 4 2 2 4 2 4 2 2 2'),
            ('8 5 4 2 2 4 2 2 5', '2 4 2 2 4 2 2 2'),
            ('0', ''),
            ('1 5', '5'),
            ('-1', ''),
            ('-1 1 2 3 4 5', ''),
        ]
    )
    def test_replace_max_with_min(self, test_marks, expected_result):
        """Test output of replace_max_with_min"""
        assert replace_max_with_min(test_marks) == expected_result

    @pytest.mark.parametrize(
        argnames='numbers_amount, numbers_array, number_to_check, expected',
        argvalues=[
            ('5', '1 2 3 4 5', '3', 'YES'),
            ('5', '1 2 3 4 5', '6', 'NO'),
        ]
    )
    def test_is_in_array(self, numbers_amount, numbers_array, number_to_check, expected):
        """Test expected input of is_in_array"""
        assert expected == is_in_array(numbers_amount, numbers_array, number_to_check)

    @pytest.mark.parametrize(
        argnames='numbers_amount, numbers_array, number_to_check, expected',
        argvalues=[
            ('5', '1 2 3 4 5', '3', '3'),
            ('5', '1 2 3 4 5', '6', ''),
            ('5', '1 2 3 1 5', '1', '1 4'),
            ('6', '5 1 5 3 4 5', '5', '1 3 6'),
            ('5', '-1000 2 3 1000 4', '1000', '4'),
        ]
    )
    def test_is_in_array(self, numbers_amount, numbers_array, number_to_check, expected):
        """Test expected input of is_in_array"""
        assert expected == get_indexes_of_equals(numbers_amount, numbers_array, number_to_check)

    @pytest.mark.parametrize(
        argnames='numbers_amount, numbers_array, expected',
        argvalues=[
            ('1', '4', 4),
            ('2', '4 4', 4),
            ('4', '-1000 -80 125 1000', 1000),
            ('3', '-1000 -999 -1000', -999)
        ]
    )
    def test_get_max_number(self, numbers_amount, numbers_array, expected):
        """Test output of get_max_number"""
        assert expected == get_max_number(numbers_amount, numbers_array)

    @pytest.mark.parametrize(
        argnames='numbers_amount, numbers_array, expected',
        argvalues=[
            ('1', '4', 1),
            ('2', '4 4', 1),
            ('4', '-1000 -80 125 1000', 4),
            ('3', '-1000 -999 -1000', 2)
        ]
    )
    def test_get_max_number(self, numbers_amount, numbers_array, expected):
        """Test output of get_max_number_index"""
        assert expected == get_max_number_index(numbers_amount, numbers_array)

    @pytest.mark.parametrize(
        argnames='numbers_amount, numbers_array, number_to_check, expected',
        argvalues=[
            ('5', '1 2 3 4 5', '6', 5),
            ('5', '1 2 3 4 5', '3', 3),
            ('4', '0 0 0 0', '3', 0),
            ('3', '-3 -2 -1', '1', -1),
            ('3', '-3 -2 -1', '-4', -3),
            ('3', '-3 -2 -1', '-2', -2),
            ('3', '-1000 0 1000', '511', 1000),
            ('3', '-1000 0 1000', '-411', 0),
            ('3', '-1000 -1000 -1000', '511', -1000),
            ('3', '-1000 -1000 -1000', '1000', -1000),
        ]
    )
    def test_get_nearest_number(self, numbers_amount, numbers_array, number_to_check, expected):
        """Test expected output of get_nearest_number"""
        assert expected == get_nearest_number(numbers_amount, numbers_array, number_to_check)

    @pytest.mark.parametrize(
        argnames='actual_input, expected_output',
        argvalues=[
            ((5, [4, 3, 3, 1, 2]), 3),
            ((8, [1, 2, 5, 3, 5, 6, 6, 5]), 5)
        ]
    )
    def test_get_second_max(self, actual_input: tuple, expected_output: str) -> None:
        """Test output"""
        assert get_second_max(actual_input[0], actual_input[1]) == expected_output
