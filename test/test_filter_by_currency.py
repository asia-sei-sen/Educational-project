# test/test_filter_by_currency.py
from generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


def test_filter_by_currency_with_matching_currency():
    # Arrange
    transactions = [
        {
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Payment 1"
        },
        {
            "operationAmount": {
                "currency": {
                    "code": "EUR"
                }
            },
            "description": "Payment 2"
        }
    ]

    # Act
    result = list(filter_by_currency(transactions, "USD"))

    # Assert
    assert len(result) == 1
    assert result[0]["description"] == "Payment 1"
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_with_non_matching_currency():
    # Arrange
    transactions = [
        {
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Payment 1"
        }
    ]

    # Act
    result = list(filter_by_currency(transactions, "EUR"))

    # Assert
    assert len(result) == 0


def test_filter_by_currency_with_empty_list():
    # Arrange
    transactions = []

    # Act
    result = list(filter_by_currency(transactions, "USD"))

    # Assert
    assert len(result) == 0


def test_filter_by_currency_returns_iterator():
    # Arrange
    transactions = [
        {
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            }
        }
    ]

    # Act
    result = filter_by_currency(transactions, "USD")

    # Assert
    assert hasattr(result, '__iter__')
    assert not hasattr(result, '__len__')  # Проверяем что это именно итератор, а не список

# Новые тесты для transaction_descriptions
def test_transaction_descriptions_returns_correct_values():
    """Проверяет корректность извлечения описаний транзакций."""
    transactions = [
        {"description": "Payment 1"},
        {"description": "Payment 2"},
        {"description": "Payment 3"}
    ]
    result = list(transaction_descriptions(transactions))
    assert result == ["Payment 1", "Payment 2", "Payment 3"]

def test_transaction_descriptions_with_empty_list():
    """Проверяет обработку пустого списка транзакций."""
    assert list(transaction_descriptions([])) == []

def test_transaction_descriptions_returns_iterator():
    """Проверяет, что функция возвращает итератор."""
    result = transaction_descriptions([{"description": "Test"}])
    assert hasattr(result, '__iter__')
    assert not hasattr(result, '__len__')


# Новые тесты для card_number_generator
def test_card_number_generator_single_value():
    """Проверяет форматирование минимального номера карты."""
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]

def test_card_number_generator_range():
    """Проверяет генерацию диапазона номеров."""
    result = list(card_number_generator(9999999999999998, 9999999999999999))
    assert result == [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ]

def test_card_number_generator_invalid_range():
    """Проверяет обработку некорректного диапазона (start > end)."""
    assert list(card_number_generator(5, 3)) == []

def test_card_number_generator_returns_iterator():
    """Проверяет, что функция возвращает итератор."""
    result = card_number_generator(1, 1)
    assert hasattr(result, '__iter__')
    assert not hasattr(result, '__len__')

# Дополнительные тесты для максимального покрытия
def test_full_coverage():
    # Проверка filter_by_currency с разными валютами
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Payment 1"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Payment 2"}
    ]
    assert len(list(filter_by_currency(transactions, "RUB"))) == 0

    # Проверка transaction_descriptions с разными описаниями
    complex_transactions = [
        {"description": "Перевод"},
        {"description": "Оплата"},
        {"description": None}  # Экстремальный случай
    ]
    assert len(list(transaction_descriptions(complex_transactions))) == 3


    # Проверка card_number_generator с граничными значениями
    assert next(card_number_generator(0, 0)) == "0000 0000 0000 0000"