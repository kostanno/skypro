from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(payment_info: str) -> str:
    """Обрабатывает строку с данными карты/счёта."""
    if len(payment_info)>0:
        parts = payment_info.split()
        number = parts[-1]
        if "Счет" in parts:
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)
            result = " ".join(parts[:-1] + [masked_number])
            return result
    return "Неверный ввод"


def get_date(date_str: str) -> str:
    """функция возврата времени"""
    if  len(date_str) > 0:
        date_part = date_str.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    return "Неверный ввод"

print(get_date("2024-03-11T02:26:18.671407"))