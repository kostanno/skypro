def filter_by_state(dicts: dict, state="EXECUTED") -> list:
    """сортировка словарей по ключу state="EXECUTED" """
    sort_dict = []
    for value in dicts:
        if value.get("state") == state:
            sort_dict.append(value)
    return sort_dict


def sort_by_date(dicta: dict, sta="True") -> list:
    """сортировка словарей по дате(по умолчанию-убывание)"""
    return sorted(dicta, key=lambda item: item["date"], reverse=sta)
