import pytest
from informatics.linear_search.linear_search_3 import get_indexes_of_equals


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
@pytest.mark.fresh
def test_is_in_array(numbers_amount, numbers_array, number_to_check, expected):
    """Test expected input of is_in_array"""
    assert expected == get_indexes_of_equals(numbers_amount, numbers_array, number_to_check)
