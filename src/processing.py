def filter_by_state(dicts, state="EXECUTED"):
    new_dict = []
    for value in dicts:
        if value.get("state") == state:
            new_dict.append(value)
        return "Такого значения нет"
    return new_dict


def sort_by_date(dicts, sta = True):
    return sorted(dicts, key=lambda item: item['date'], reverse=True)
