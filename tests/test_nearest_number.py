import pytest
from informatics.linear_search.nearest_number import get_nearest_number


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
def test_get_nearest_number(numbers_amount, numbers_array, number_to_check, expected):
    """Test expected output of get_nearest_number"""
    assert expected == get_nearest_number(numbers_amount, numbers_array, number_to_check)
