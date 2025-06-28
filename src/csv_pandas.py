import csv
import openpyxl
import pandas
import pandas as pd


def way_csv(way_csv:str) -> None:
    with open(way_csv) as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row


def way_excel(way_excel:str) -> None:
    excel_data = pd.read_excel(way_excel)
    print(excel_data)
