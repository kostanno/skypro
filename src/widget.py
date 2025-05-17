from src.masks import mask_account_number
from src.masks import mask_card_number


def process_payment_info(payment_info: str) -> str:
    """Обрабатывает строку с данными карты/счёта."""
    parts = payment_info.split()
    number = parts[-1]
    if "Счет" in parts:
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)
    result = " ".join(parts[:-1] + [masked_number])
    return result


def get_date(date_str: str) -> str:
    """функция возврата времени"""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
