import csv
from unittest.mock import mock_open, patch, MagicMock
import pytest
from src.csv_pandas import way_csv,way_excel


def test_way_csv_file_not_found():
    """Тест с проверкой обработки отсутствующего файла."""
    with patch("builtins.open", side_effect=FileNotFoundError("File not found")):
        with pytest.raises(FileNotFoundError):
            way_csv("non_existent_file.csv")


def test_way_csv_empty_file():
    """Тест с пустым CSV (мок пустого файла)."""
    m = mock_open(read_data="name,age,city\n")  # Только заголовок
    with patch("builtins.open", m):
        way_csv("empty.csv")


def test_way_excel_empty_file():
    """Тест с пустым Excel-файлом (мок пустого DataFrame)."""
    mock_empty_data = MagicMock()
    mock_empty_data.empty = True  # Эмулируем пустой DataFrame

    with patch("pandas.read_excel", return_value=mock_empty_data):
        way_excel("empty.xlsx")  # Проверяем, что функция не падает на пустом файле