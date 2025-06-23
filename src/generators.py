def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount")
        currency_info = operation_amount.get("currency")
        currency_code = currency_info.get("code")
        if currency_code == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> iter:
    """Генератор, который возвращает описание каждой транзакции по очереди"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> iter:
    """Генератор который выдает номера банковских карт"""
    while start <= stop:
        card_number = f"{start:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        start += 1
