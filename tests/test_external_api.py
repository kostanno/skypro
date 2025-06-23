from src.external_api import transaction
import pytest
from unittest.mock import patch, Mock


def test_transaction_rub():
    """обработкa транзакции в рублях"""
    trans = [
        {
            "operationAmount": {
                "amount": "1000.0",
                "currency": {
                    "code": "RUB"
                }
            }
        }
    ]
    assert transaction(trans) == 1000.0


def test_transaction_unsupported_currency():
    """обработкa транзакции с неподдерживаемой валютой"""
    trans = [
        {
            "operationAmount": {
                "amount": "10.0",
                "currency": {
                    "code": "GBP"
                }
            }
        }
    ]
    with pytest.raises(ValueError, match="Неподдерживаемая валюта"):
        transaction(trans)


@patch('requests.get')
def test_transaction_usd(mock_get):
    """обработкa транзакции в долларах"""
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value = mock_response
    trans = [
        {
            "operationAmount": {
                "amount": "10.0",
                "currency": {
                    "code": "USD"
                }
            }
        }
    ]
    assert transaction(trans) == 750.0  # 10 USD * 75 RUB/USD
