import pytest
from unittest.mock import patch, MagicMock
from src.re_collection import process_bank_search, process_bank_operations
import re
from collections import Counter

def test_process_bank_search_case_insensitive(sample_transactions):
    """Тест регистронезависимого поиска"""
    result_lower = process_bank_search(sample_transactions, "перевод")
    result_upper = process_bank_search(sample_transactions, "ПЕРЕВОД")
    assert len(result_lower) == len(result_upper) == 2


def test_process_bank_search_empty_data():
    """Тест с пустым списком операций"""
    result = process_bank_search([], "перевод")
    assert len(result) == 0


@patch('your_module.re.compile')
def test_process_bank_search_re_error(mock_compile, sample_transactions):
    """Тест обработки ошибки регулярного выражения"""
    mock_compile.side_effect = re.error("test error")
    result = process_bank_search(sample_transactions, "перевод")
    assert len(result) == 0
    mock_compile.assert_called_once()


@patch('your_module.Counter')
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
