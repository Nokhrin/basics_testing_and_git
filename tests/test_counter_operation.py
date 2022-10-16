import pytest
from informatics.linear_search.counter_operation import replace_max_with_min


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
def test_replace_max_with_min(test_marks, expected_result):
    """Test output of replace_max_with_min"""
    assert replace_max_with_min(test_marks) == expected_result
