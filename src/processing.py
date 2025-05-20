def filter_by_state(dict,state="EXECUTED"):
    new_dict = []
    for value in dict :
        if value.get("state") == state:
            new_dict.append(value)
    return new_dict


def sort_by_date(dict, sta = True):
    return sorted(dict, key=lambda item: item['date'], reverse=True)





