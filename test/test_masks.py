import pytest

from src.masks import (
    mask_account_number,
    mask_credit_card,
)


def test_card_masking():
    """Тест маскировки номера карты."""
    assert mask_credit_card("1234567890123456") == "1234 56** **** 3456"
    assert mask_credit_card("1234 5678 9012 3456") == "1234 56** **** 3456"
    assert mask_credit_card("1234") == "Некорректный номер карты"  # Исправлена опечатка (лишний пробел)

def test_account_masking():
    """Тест маскировки номера счета."""
    assert mask_account_number("1234567890") == "**7890"
    assert mask_account_number("1234 5678 90") == "**7890"
    assert mask_account_number("123") == "Некорректный номер счета"

# Новые тесты для дополнительных случаев
def test_card_edge_cases():
    """Тест граничных случаев для карт."""
    assert mask_credit_card("") == "Некорректный номер карты"  # Пустая строка
    assert mask_credit_card("abcdefghijklmnop") == "Некорректный номер карты"  # Буквы
    assert mask_credit_card("12345678901234567890") == "Некорректный номер карты"  # Слишком длинный номер
    assert mask_credit_card("!@#$%^&*()") == "Некорректный номер карты"  # Специальные символы

def test_account_edge_cases():
    """Тест граничных случаев для счетов."""
    assert mask_account_number("") == "Некорректный номер счета"  # Пустая строка
    assert mask_account_number("abc") == "Некорректный номер счета"  # Буквы
    assert mask_account_number("12345678901234567890") == "Некорректный номер счета"  # Слишком длинный номер
    assert mask_account_number("!@#$%^&*()") == "Некорректный номер счета"  # Специальные символы

# Фикстуры для параметризованных тестов
@pytest.fixture
def card_samples():
    return [
        ("1111222233334444", "1111 22** **** 4444"),
        ("9999 8888 7777 6666", "9999 88** **** 6666")
    ]

@pytest.fixture
def account_samples():
    return [
        ("12345678", "**5678"),
        ("8765 4321", "**4321")
    ]

# Параметризованные тесты
@pytest.mark.parametrize("card_num, expected", [
    ("5555666677778888", "5555 66** **** 8888"),
    ("5555 6666 7777 8888", "5555 66** **** 8888"),
    ("1", "Некорректный номер карты"),
    ("", "Некорректный номер карты"),   # Пустая строка
])
def test_parametrized_card(card_num, expected):
    assert mask_credit_card(card_num) == expected

@pytest.mark.parametrize("acc_num, expected", [
    ("11223344", "**3344"),
    ("11 22 33 44", "**3344"),
    ("1", "Некорректный номер счета"),
    ("", "Некорректный номер счета"),   # Пустая строка
])
def test_parametrized_account(acc_num, expected):
    assert mask_account_number(acc_num) == expected