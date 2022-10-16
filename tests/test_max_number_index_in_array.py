import pytest
from informatics.linear_search.max_number_index_in_array import get_max_number_index


@pytest.mark.parametrize(
    argnames='numbers_amount, numbers_array, expected',
    argvalues=[
        ('1', '4', 1),
        ('2', '4 4', 1),
        ('4', '-1000 -80 125 1000', 4),
        ('3', '-1000 -999 -1000', 2)
    ]
)
def test_get_max_number(numbers_amount, numbers_array, expected):
    """Test output of get_max_number_index"""
    assert expected == get_max_number_index(numbers_amount, numbers_array)
