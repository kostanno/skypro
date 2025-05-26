import pytest


from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


@pytest.mark.parametrize("payment_info", [("Maestro 1596837868705199"), ("Счет 64686473678894779589"),
("Master Card 7158300734726758"), ("Счет 35383033474447895560"), ("Visa Classic 6831982476737658"), ("Visa Gold 5999414228426353")])
def test_mask_account_card_param(payment_info):
    assert mask_account_card(payment_info)


def test_get_date():
    assert get_date("") == "Неверный ввод"


def test_get_date_split():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
