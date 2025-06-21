from src.utils import load_trans
import json


def test_load_trans_valid_list(tmp_path):
    """Тест загрузки корректного JSON-файла со списком транзакций"""
    test_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    file_path = tmp_path / "transactions.json"
    with open(file_path, 'w') as f:
        json.dump(test_data, f)
    assert load_trans(file_path) == test_data


def test_load_trans_file_not_found():
    """Тест обработки случая, когда файл не найден"""
    non_existent_file = "non_existent_file.json"
    assert load_trans(non_existent_file) == []
