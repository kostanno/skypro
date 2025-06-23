import os
from dotenv import load_dotenv
import requests

load_dotenv()


API_KEY = os.getenv("API_KEY")


def transaction(trans: dict) -> float:
    """Обрабатывает транзакцию и возвращает сумму в рублях"""
    for transs in trans:
        operation_amount = transs["operationAmount"]
        amount_info = operation_amount["amount"]
        currency_info = operation_amount["currency"]
        currency_code = currency_info["code"]
        amount = float(amount_info)
        if currency_code == "RUB":
            return amount
        elif currency_code == "USD":
            url = "https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB"
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            rate = data["rates"]["RUB"]
            return amount * rate
        elif currency_code == "EUR":
            url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&symbols=RUB"
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            rate = data["rates"]["RUB"]
            return amount * rate
        else:
            raise ValueError(f"{"Неподдерживаемая валюта"}")
