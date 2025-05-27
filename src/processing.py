from typing import  Any,Union

def filter_by_state(dicts, state="EXECUTED") -> Union[list, str]:
    new_dict = []
    for value in dicts:
        if value.get("state") == state:
            new_dict.append(value)
        return "Такого значения нет"
    return new_dict


def sort_by_date(dicts: list, sta = True) -> list:
    return sorted(dicts, key=lambda item: item['date'], reverse=True)


# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))