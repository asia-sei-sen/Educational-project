def mask_credit_card(card_number: str) -> str:
    """Маскирует номер кредитной карты, оставляя первые 6 и последние 4 цифры."""
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16 or not card_number.isdigit():
        return "Некорректный номер карты"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета, оставляя только последние 4 цифры."""
    account_number = account_number.replace(" ", "")
    if len(account_number) < 4 or not account_number.isdigit():
        return "Некорректный номер счета"
    return f"**{account_number[-4:]}"