from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_account() -> None:
    assert get_mask_account("12345678912345678912") == "**8912"


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"
