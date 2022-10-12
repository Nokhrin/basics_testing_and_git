import pytest
from informatics.linear_search.linear_search_2 import is_in_array


@pytest.mark.parametrize(
    argnames='numbers_amount, numbers_array, number_to_check, expected',
    argvalues=[
        ('5', '1 2 3 4 5', '3', 'YES'),
        ('5', '1 2 3 4 5', '6', 'NO'),
    ]
)
def test_is_in_array(numbers_amount, numbers_array, number_to_check, expected):
    """Test expected input of is_in_array"""
    assert expected == is_in_array(numbers_amount, numbers_array, number_to_check)
