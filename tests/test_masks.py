from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("736541084305874305") == "**4305"
    assert get_mask_account("") == ""


def test_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("4222222222222") == "4222 22** *222 2"
    assert get_mask_card_number("6762123456789012345") == "6762 12** **** ***2 345"
    assert get_mask_card_number("") == ""