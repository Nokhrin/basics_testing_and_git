import pytest
from informatics.linear_search.auditing import get_two_min_values


@pytest.mark.parametrize(
    argnames='numbers_amount, numbers_array, expected',
    argvalues=[
        ('5', '10 2 3 1 5', '1 2'),
    ]
)
def test_get_two_min_values(numbers_amount, numbers_array, expected):
    """Test output of get_two_min_values"""
    assert expected == get_two_min_values(numbers_amount, numbers_array)
