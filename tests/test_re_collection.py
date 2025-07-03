import pytest
from unittest.mock import mock_open, patch, MagicMock
from src.re_collection import process_bank_search, process_bank_operations
import re
from collections import Counter

@pytest.fixture
def sample_transactions():
    return [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Открытие вклада", "amount": 500},
        {"description": "Перевод с карты на карту", "amount": 200},
        {"description": "Покупка в магазине", "amount": 50},
        {"description": None, "amount": 300},  # Невалидное описание
        {"no_description": "Нет поля description", "amount": 400},
    ]


def test_process_bank_search_empty_data():
    """Тест с пустым списком операций"""
    result = process_bank_search([], "перевод")
    assert len(result) == 0


@pytest.fixture
def sample_operations():
    return [
        {"description": "Перевод организации", "amount": 100, "status": "EXECUTED"},
        {"description": "Открытие вклада", "amount": 500, "status": "EXECUTED"},
        {"description": "Перевод с карты на карту", "amount": 200, "status": "CANCELED"},
        {"description": "Покупка в магазине", "amount": 50, "status": "EXECUTED"},
        {"description": "Вклад под проценты", "amount": 1000, "status": "PENDING"},
        {"description": None, "amount": 300},  # Невалидное описание
        {"no_description": "Нет поля description", "amount": 400},  # Нет поля description
    ]


@patch('src.re_collection.re.compile')
def test_process_bank_search_re_error(mock_compile, sample_transactions):
    """Тест обработки ошибки регулярного выражения"""
    mock_compile.side_effect = re.error("test error")
    result = process_bank_search(sample_transactions, "перевод")
    assert len(result) == 0
    mock_compile.assert_called_once()


@patch('src.re_collection.Counter')
def test_process_bank_operations_counter_updates(mock_counter, sample_operations):
    """Тест правильности обновления счетчика"""
    real_counter = Counter()
    mock_counter.return_value = real_counter
    categories = ["Перевод", "Вклад"]
    result = process_bank_operations(sample_operations, categories)
    assert result["Перевод"] == 2
    assert result["Вклад"] == 2
    mock_counter.assert_called_once()


def test_process_bank_operations_empty_categories(sample_operations):
    """Тест с пустым списком категорий"""
    result = process_bank_operations(sample_operations, [])
    assert result == {}


@patch('src.re_collection.re.compile')
def test_process_bank_search_re_called_correctly(mock_compile, sample_transactions):
    """Тест правильности вызова re.compile"""
    mock_pattern = MagicMock()
    mock_compile.return_value = mock_pattern

    process_bank_search(sample_transactions, "перевод")

    mock_compile.assert_called_once_with(re.escape("перевод"), re.IGNORECASE)
    assert mock_pattern.search.call_count == 4