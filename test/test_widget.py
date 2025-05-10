import pytest

from src.widget import (
    mask_account_card,
)


# Общая фикстура для всех валидных данных
@pytest.fixture(params=[
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("MasterCard Gold 5555666677778888", "MasterCard Gold 5555 66** **** 8888"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def valid_case(request):
    return request.param

# Фикстура для невалидных данных
@pytest.fixture(params=[
    ("", "Некорректный ввод"),
    ("Visa Platinum invalid", "Некорректный формат карты"),
    ("Unknown Card 1234567890123456", "Некорректный формат карты"),
    ("Счет без номера", "Некорректный формат счета"),
    ("Visa Platinum !@#$%^&*()", "Некорректный формат карты"),  # Специальные символы
])
def invalid_case(request):
    return request.param

def test_valid_masking(valid_case):
    """Параметризованный тест для валидных данных"""
    input_value, expected_output = valid_case
    assert mask_account_card(input_value) == expected_output

def test_invalid_inputs(invalid_case):
    """Параметризованный тест для невалидных данных"""
    input_value, error_message = invalid_case
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(input_value)

def test_name_preservation():
    """Дополнительный тест на сохранение названия"""
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert "Visa Platinum" in result

# Новые тесты для дополнительных случаев
def test_edge_cases():
    """Тест граничных случаев."""
    assert mask_account_card("12345678901234567890") == "Некорректный ввод"  # Слишком длинный номер
    assert mask_account_card("123") == "Некорректный ввод"  # Слишком короткий номер
    assert mask_account_card("Visa Platinum ") == "Некорректный ввод"  # Пробел в конце