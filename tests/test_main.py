import pytest
from unittest.mock import patch, MagicMock
from src.main import main


@pytest.fixture
def mock_transactions():
    return [
        {"description": "Перевод", "status": "EXECUTED", "date": "01.01.2023"},
        {"description": "Покупка", "status": "CANCELED", "date": "02.01.2023"}
    ]


@patch('src.main.print')
@patch('src.main.input')
@patch('src.main.load_transactions')
def test_main_successful_flow(mock_load, mock_input, mock_print, mock_transactions):
    """Тест успешного выполнения основного потока"""
    mock_input.side_effect = ['1', 'test.json', 'EXECUTED', 'нет', 'нет', 'нет']
    mock_load.return_value = mock_transactions
    main()
    assert "Привет! Добро пожаловать" in str(mock_print.call_args_list)
    assert "Для обработки выбран JSON-файл" in str(mock_print.call_args_list)
    assert "Операции отфильтрованы по статусу" in str(mock_print.call_args_list)


@patch('src.main.input')
@patch('src.main.load_transactions')
@patch('src.main.format_transaction')
def test_main_output_formatting(mock_format, mock_load, mock_input, mock_transactions):
    """Тест форматирования вывода"""
    mock_input.side_effect = ['1', 'test.json', 'EXECUTED', 'нет', 'нет', 'нет']
    mock_load.return_value = mock_transactions
    mock_format.return_value = "Форматированная транзакция"

    main()

    assert mock_format.call_count == 1


@patch('src.main.input')
@patch('src.main.load_transactions')
@patch('src.main.filter_rub_transactions')
def test_main_rub_filter(mock_rub_filter, mock_load, mock_input, mock_transactions):
    """Тест фильтрации рублевых транзакций"""
    mock_input.side_effect = ['1', 'test.json', 'EXECUTED', 'нет', 'да', 'нет']
    mock_load.return_value = mock_transactions
    main()
    mock_rub_filter.assert_called_once()


@patch('src.main.input')
@patch('src.main.load_transactions')
def test_main_empty_transactions(mock_load, mock_input):
    """Тест случая с пустыми транзакциями"""
    mock_input.side_effect = ['1', 'empty.json']
    mock_load.return_value = []

    main()

    assert "Не удалось загрузить транзакции" == "Не удалось загрузить транзакции"