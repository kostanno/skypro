import csv
import pandas as pd


def way_csv(way_csv: str) -> list:
    """Функция возвращает словарь из CSV файла"""
    dicts = []
    with open(way_csv) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dicts.append(row)
        return dicts


def way_excel(way_excel: str) -> list:
    """Функция возвращает словарь из Excell файла"""
    my_excell = []
    excel_data = pd.read_excel(way_excel)
    for _ in excel_data:
        my_excell.append(_)
    return my_excell
