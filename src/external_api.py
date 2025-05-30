"""
Модуль для взаимодействия с внешним API конвертации валют.
"""

import os
import requests


API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции из USD или EUR в рубли (RUB).

    :param transaction: Словарь с ключами 'amount' и 'currency'.
    :return: Сумма в рублях (float). Если валюта уже в RUB, возвращается исходная сумма.
    """
    currency = transaction.get("currency")
    amount = transaction.get("amount")

    if currency == "RUB":
        return float(amount)

    if currency not in ("USD", "EUR") or not API_KEY:
        return 0.0

    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount,
    }

    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params, headers=headers)
        response.raise_for_status()
        result = response.json()
        return float(result.get("result", 0.0))
    except Exception as e:
        print(f"Ошибка при конвертации валюты: {e}")
        return 0.0
