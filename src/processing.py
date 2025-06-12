def filter_by_state(dicta, state="EXECUTED"):
    new_dict = []
    for value in dicta:
        if value.get("state") == state:
            new_dict.append(value)
    return new_dict


def sort_by_date(dicta, sta = True):
    return sorted(dicta, key=lambda item: item['date'], reverse=True)
