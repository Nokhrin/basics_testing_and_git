import pytest
from informatics.linear_search.columns import is_number_in_column


@pytest.mark.parametrize(
    argnames='actual_num, actual_rows, actual_matrix, expected_output',
    argvalues=[
        (1789, 1, [[1789]], "YES"),
        (9, 1, [[1789]], "NO"),
        (5, 2, [[4, 5], [2, 3]], "NO\nYES"),
        (5, 2, [[0, 0], [0, 0]], "NO\nNO"),
        (5, 2, [[5, 5], [0, 5]], "YES\nYES"),
        (5, 3, [[5, 6, 7], [1, 2, 3], [-9, -1231, 33]], "YES\nNO\nNO"),
    ]
)
@pytest.mark.fresh
def test_is_number_in_column(actual_num, actual_rows, actual_matrix, expected_output):
    """Test output"""
    assert is_number_in_column(actual_num, actual_rows, actual_matrix) == expected_output
