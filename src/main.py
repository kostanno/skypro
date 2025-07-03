import json
import csv
import openpyxl
from datetime import datetime
from typing import List, Dict


def load_transactions(file_path: str, file_type: str) -> List[Dict]:
    """Загружает транзакции из файла указанного типа"""
    try:
        if file_type == "json":
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif file_type == "csv":
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        elif file_type == "xlsx":
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            headers = [cell.value for cell in sheet[1]]
            return [
                dict(zip(headers, [cell.value for cell in row]))
                for row in sheet.iter_rows(min_row=2)
            ]
        else:
            return []
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрует транзакции по статусу (без учета регистра)"""
    status_lower = status.lower()
    return [
        t for t in transactions
        if isinstance(t, dict) and t.get('status', '').lower() == status_lower
    ]


def sort_transactions(transactions: List[Dict], reverse: bool = False) -> List[Dict]:
    """Сортирует транзакции по дате"""

    def get_date(transaction):
        date_str = transaction.get('date', '')
        try:
            return datetime.strptime(date_str, '%d.%m.%Y')
        except ValueError:
            return datetime.min

    return sorted(
        transactions,
        key=get_date,
        reverse=reverse
    )


def filter_rub_transactions(transactions: List[Dict]) -> List[Dict]:
    """Фильтрует только рублевые транзакции"""
    return [
        t for t in transactions
        if isinstance(t, dict) and t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']


def filter_by_description(transactions: List[Dict], search_word: str) -> List[Dict]:
    """Фильтрует транзакции по ключевому слову в описании"""
    search_lower = search_word.lower()
    return [
        t for t in transactions
        if isinstance(t, dict) and search_lower in t.get('description', '').lower()]


def format_transaction(transaction: Dict) -> str:
    """Форматирует транзакцию для вывода"""
    date = transaction.get('date', 'Дата не указана')
    description = transaction.get('description', 'Описание отсутствует')
    from_info = transaction.get('from', '')
    to_info = transaction.get('to', '')

    def mask_card_number(text: str) -> str:

        if not text:
            return ''
        parts = text.split()
        number = parts[-1]
        if len(number) == 16 and number.isdigit():
            return f"{' '.join(parts[:-1])} {number[:4]} {number[4:6]}** **** {number[-4:]}"
        elif len(number) >= 4:
            return f"{' '.join(parts[:-1])} **{number[-4:]}"
        return text
    from_info = mask_card_number(from_info)
    to_info = mask_card_number(to_info)
    amount_info = transaction.get('operationAmount', {})
    amount = amount_info.get('amount', '0')
    currency = amount_info.get('currency', {}).get('code', '')
    result = [f"{date} {description}"]
    if from_info and to_info:
        result.append(f"{from_info} -> {to_info}")
    elif from_info:
        result.append(from_info)
    elif to_info:
        result.append(to_info)
    result.append(f"Сумма: {amount} {currency}")
    return '\n'.join(result)


def main():
    """Функция которая отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    file_choice = input("Введите номер пункта меню: ").strip()
    file_types = {
        '1': ('json', 'JSON'),
        '2': ('csv', 'CSV'),
        '3': ('xlsx', 'XLSX')
    }
    if file_choice not in file_types:
        print("Неверный выбор формата файла.")
        return
    file_ext, file_type_name = file_types[file_choice]
    file_path = input(f"Введите путь к {file_type_name}-файлу: ").strip()
    print(f"\nДля обработки выбран {file_type_name}-файл.")
    transactions = load_transactions(file_path, file_ext)
    if not transactions:
        print("Не удалось загрузить транзакции или файл пуст.")
        return
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        print("\nДоступные для фильтровки статусы:", ', '.join(valid_statuses))
        status = input("Введите статус, по которому необходимо выполнить фильтрацию: ").strip().upper()
        if status in valid_statuses:
            break
        print(f'Статус операции "{status}" недоступен.')
    filtered = filter_by_status(transactions, status)
    print(f'\nОперации отфильтрованы по статусу "{status}"')
    if not filtered:
        print("Не найдено ни одной транзакции с указанным статусом.")
        return
    sort_choice = input("\nОтсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_choice == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = order.startswith('убы')
        filtered = sort_transactions(filtered, reverse)
    rub_only = input("\nВыводить только рублевые транзакции? (Да/Нет): ").strip().lower()
    if rub_only == 'да':
        filtered = filter_rub_transactions(filtered)
    search_choice = input("\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").strip().lower()
    if search_choice == 'да':
        search_word = input("Введите слово для поиска в описании: ").strip()
        filtered = filter_by_description(filtered, search_word)
    print("\nРаспечатываю итоговый список транзакций...\n")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print(f"Всего банковских операций в выборке: {len(filtered)}\n")
    for transaction in filtered:
        print(format_transaction(transaction))
        print()
