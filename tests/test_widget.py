import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "t_input, t_output",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(t_input, t_output):
    assert mask_account_card(t_input) == t_output


@pytest.mark.parametrize(
    "t_input, t_output",
    [
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        ("1995-05-20T15:30:45.123456", "20.05.1995"),
        ("2000-02-29T12:00:00.000000", "29.02.2000"),
    ],
)
def test_get_date(t_input, t_output):
    assert get_date(t_input) == t_output
