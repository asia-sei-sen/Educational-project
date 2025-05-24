import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    # Эмулируем ответ API
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 100.0}

    # Тестируемую транзакцию
    transaction = {"amount": 1, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert isinstance(result, float)
    assert result == 100.0
    mock_get.assert_called_once()