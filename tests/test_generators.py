import pytest


from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def test_filter_by_currency():
    """функция  фильтрует транзакции по валюте"""
    filtered_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(filtered_transactions) == 3


def test_filter_by_currency1():
    """функция возвращает пустой список"""
    filtered_transactions = list(filter_by_currency(transactions, "YYY"))
    assert filtered_transactions == []


def test_filter_by_currency2():
    """функция  обрабатывает пустой список транзакций"""
    filtered_transactions = list(filter_by_currency([], "USD"))
    assert filtered_transactions == []


def test_transaction_descriptions():
    """функция  фильтрует транзакции по описанию операции """
    filtered_transactions = list(transaction_descriptions(transactions))
    assert len(filtered_transactions) == 5


def test_transaction_descriptions1():
    """функция  обрабатывает пустой список транзакций"""
    filtered_transactions = list(transaction_descriptions([]))
    assert filtered_transactions == []


def test_card_number_generator():
    """функция  форматирования номеров карт"""
    numbers = list(card_number_generator(0, 10))
    for number in numbers:
        parts = number.split(' ')
        assert len(parts) == 4


@pytest.fixture
def sample_card_numbers():
    """Фикстура с примерами ожидаемых номеров карт для тестирования."""
    return [
        "0000 0000 0000 0000",
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]


@pytest.mark.parametrize("start, end, expected_first, expected_last", [
    (0, 1, "0000 0000 0000 0000", "0000 0000 0000 0001"),
    (9998, 9999, "0000 0000 0000 9998", "0000 0000 0000 9999"),
    (10000, 10001, "0000 0000 0001 0000", "0000 0000 0001 0001"),
    (9999999999999998, 9999999999999999, "9999 9999 9999 9998", "9999 9999 9999 9999"),
])
def test_generator_values(start, end, expected_first, expected_last):
    """Тест проверяет корректность первого и последнего значения в диапазоне."""
    numbers = list(card_number_generator(start, end))
    assert numbers[0] == expected_first
    assert numbers[-1] == expected_last
