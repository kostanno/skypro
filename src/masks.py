def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта."""
    if len(account_number) == 20:
        return "**" + account_number[-4:]
    return "неверный ввод"

def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return "неверынй ввод"
# print(get_mask_account("12345678912354567"))