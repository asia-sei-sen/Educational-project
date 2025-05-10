import re
from datetime import (
    datetime,
)

from src.masks import (
    mask_account_number,
    mask_credit_card,
)


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO в строку 'ДД.ММ.ГГГГ'."""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return "Некорректный формат даты"


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    Args:
        info: Строка формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".

    Returns:
        Строка с маскированным номером карты/счета.
    """
    if not info or not isinstance(info, str):
        raise ValueError("Некорректный ввод: ожидается не пустая строка")

    if info.startswith("Счет"):
        parts = info.split()
        if len(parts) < 2:
            raise ValueError("Некорректный формат счета")
        account_number = "".join(parts[1:])
        masked = mask_account_number(account_number)
        return f"Счет {masked}"

    match = re.search(r"(\d[\d\s]+\d)$", info)
    if not match:
        raise ValueError("Некорректный формат карты")

    card_number = match.group(1).replace(" ", "")

    # Проверка на длину номера карты
    if len(card_number) != 16:
        raise ValueError("Некорректный номер карты")

    card_name = info[: match.start()].strip()
    masked = mask_credit_card(card_number)

    return f"{card_name} {masked}"