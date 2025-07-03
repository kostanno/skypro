import pytest


from src.processing import filter_by_state


def test_filter_by_state() -> None:
    assert filter_by_state([{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == []


@pytest.fixture
def coll() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {" "}]


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Payment 1", "state": "EXECUTED"},
        {"description": "Payment 2", "state": "PENDING"},
        {"description": "Payment 3", "state": "EXECUTED"},
        {"description": "Payment 4", "state": "CANCELED"},
        {"description": "Payment 5"},  # Нет поля state
        {"state": "EXECUTED"},  # Только поле state
    ]


def test_filter_executed(sample_transactions):
    """Тест фильтрации по статусу EXECUTED (по умолчанию)"""
    result = filter_by_state(sample_transactions)
    assert len(result) == 3
    assert all(t.get("state") == "EXECUTED" for t in result)


def test_filter_pending(sample_transactions):
    """Тест фильтрации по статусу PENDING"""
    result = filter_by_state(sample_transactions, "PENDING")
    assert len(result) == 1
    assert result[0]["description"] == "Payment 2"


def test_filter_canceled(sample_transactions):
    """Тест фильтрации по статусу CANCELED"""
    result = filter_by_state(sample_transactions, "CANCELED")
    assert len(result) == 1
    assert result[0]["description"] == "Payment 4"

def test_filter_no_state_field(sample_transactions):
    """Тест фильтрации транзакций без поля state"""
    result = filter_by_state(sample_transactions, "EXECUTED")
    # Проверяем, что транзакция без поля state не попала в результат
    assert len([t for t in result if "description" in t and t["description"] == "Payment 5"]) == 0


def test_filter_empty_list():
    """Тест с пустым списком транзакций"""
    result = filter_by_state([], "EXECUTED")
    assert len(result) == 0


def test_filter_only_state_field(sample_transactions):
    """Тест фильтрации транзакции с только полем state"""
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert any("description" not in t for t in result)  # Проверяем наличие транзакции без description


def test_filter_invalid_state(sample_transactions):
    """Тест фильтрации по несуществующему статусу"""
    result = filter_by_state(sample_transactions, "INVALID_STATE")
    assert len(result) == 0

def test_filter_case_sensitivity():
    """Тест чувствительности к регистру"""
    transactions = [
        {"description": "Payment 1", "state": "executed"},
        {"description": "Payment 2", "state": "EXECUTED"},
    ]
    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]["description"] == "Payment 2"