import logging

# Создаем логер для модуля masks
logger_masks = logging.getLogger('masks')

# Настраиваем формат и хэндлер для логов
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler = logging.FileHandler('./logs/masks.log', mode='w')
handler.setFormatter(formatter)
logger_masks.addHandler(handler)
logger_masks.setLevel(logging.DEBUG)

# Декоратор для логирования функций
def log(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger_masks.info(f'{func.__name__} успешно выполнена.')
            return result
        except Exception as e:
            logger_masks.error(f'{func.__name__} завершилась с ошибкой: {e}')
            raise
    return wrapper

@log
def mask_credit_card(card_number: str) -> str:
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный номер карты")
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_card

@log
def mask_account_number(account_number: str) -> str:
    account_number = account_number.replace(" ", "")
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Некорректный номер счета")
    masked_account = f"**{account_number[-4:]}"
    return masked_account