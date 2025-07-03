# import logging
#
#
# # logger = logging.getLogger("masks")
# # file_handler = logging.FileHandler("../logs/masks.log")
# # file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
# # file_handler.setFormatter(file_formatter)
# # logger.addHandler(file_handler)
# # logger.setLevel(logging.DEBUG)
# # filemode = "w"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта."""
    if len(account_number) == 20:
        # logger.info(f"{"Выполнено"}")
        return "**" + account_number[-4:]
    # logger.error(f"{"не Выполнено"}")
    return "неверный ввод"


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    if len(card_number) == 16:
        # logger.info(f"{"Выполнено"}")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    # logger.error(f"{"не Выполнено"}")
    return "неверынй ввод"
