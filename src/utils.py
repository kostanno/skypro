import json


def load_trans(file_way):
    """данные о транзакциях из JSON файла"""
    try:
        with open(file_way) as f:
            way = json.load(f)
            if isinstance(way, list):
                return way
            else:
                return []
    except FileNotFoundError:
        return []
