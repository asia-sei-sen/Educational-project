import logging
import json
from typing import List, Dict

# Создаем логер для модуля utils
logger_utils = logging.getLogger('utils')

# Настраиваем формат и хэндлер для логов
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler = logging.FileHandler('./logs/utils.log', mode='w')
handler.setFormatter(formatter)
logger_utils.addHandler(handler)
logger_utils.setLevel(logging.DEBUG)

# Декоратор для логирования функций
def log(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger_utils.info(f'{func.__name__} успешно выполнена.')
            return result
        except Exception as e:
            logger_utils.error(f'{func.__name__} завершилась с ошибкой: {e}')
            raise
    return wrapper

@log
def load_json_file(filepath: str) -> List[Dict]:
    """
    Загружает данные из JSON-файла и возвращает список словарей.
    Если возникают проблемы — возвращается пустой список.
    """
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []