def mask_account_card(mask_card:str) -> str:
    global byk
    global num
    for card in mask_card:
        if card.isdigit():
            num+= card
        else:
            byk+= card
    return f"{byk} {num}"


byk = ""
num = ""


def get_mask_account(get_card: str) -> str:
    """функция маскировки номера банковского счета"""
    if len(num) == 20:
        return f"{byk} {2 * '*'}{num[-4:]}"
    elif len(num) == 16:
        return f"{byk} {num[:4]} {num[5:7]}{2 * "*"} {4 * "*"} {num[-4:]}"
    else:
        return f"Неправильный ввод"