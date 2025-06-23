import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
filemode = "w"


def load_trans(file_way):
    """данные о транзакциях из JSON файла"""
    try:
        logger.info(f"читаем данные из файла")
        with open(file_way) as f:
            way = json.load(f)
            if isinstance(way, list):
                logger.info(f"Проверка файла на соответствие")
                return way
            else:
                return []
    except FileNotFoundError:
        logger.error(f"Произошла ошибка")
        return []
