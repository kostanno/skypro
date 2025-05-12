from typing import Union


def get_mask_account(get_card: Union[int]) -> str:
    """функция маскировки номера банковского счета"""
    mask_card = str(get_card)
    if len(mask_card) == 20:
        return 2 * "*" + mask_card[-4:]
    else:
        return f"Неправильный ввод вы ввели {len(mask_card)} цифр"


def get_mask_card_number(num_card: Union[int]) -> str:
    """функция маскировки номера банковской карты"""
    mask_num_card = str(num_card)
    if len(mask_num_card) == 16:
        return f"{mask_num_card[:4]} {mask_num_card[5:7] + 2 * "*"} {4 * "*"} {mask_num_card[-4:]}"
    else:
        return f"Неправильный ввод вы ввели {len(mask_num_card)} цифр"
