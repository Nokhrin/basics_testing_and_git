import pytest
from informatics.linear_search.silver_medal import get_second_max


@pytest.mark.parametrize(
    argnames='actual_input, expected_output',
    argvalues=[
        ((5, [4, 3, 3, 1, 2]), 3),
        ((8, [1, 2, 5, 3, 5, 6, 6, 5]), 5)
    ]
)
def test_get_second_max(actual_input: tuple, expected_output: str) -> None:
    """Test output"""
    assert get_second_max(actual_input[0], actual_input[1]) == expected_output
