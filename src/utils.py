"""
Модуль utils.

Содержит утилитарные функции для работы с файлами.
"""

import json
from typing import List, Dict


def load_json_file(filepath: str) -> List[Dict]:
    """
    Загружает данные из JSON-файла и возвращает список словарей.

    :param filepath: Путь к JSON-файлу.
    :return: Список словарей с данными из файла. Пустой список, если файл не найден,
             пустой, или не содержит список.
    """
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
