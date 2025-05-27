from typing import Union


def filter_by_state(dicts, state="EXECUTED") -> Union[list, str]:
    new_dict = []
    for value in dicts:
        if value.get("state") == state:
            new_dict.append(value)
        return "Такого значения нет"
    return new_dict


def sort_by_date(dicts: list, sta=True) -> list:
    return sorted(dicts, key=lambda item: item['date'], reverse=True)
