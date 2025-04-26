from datetime import datetime
from typing import List, Dict, Optional, Literal

def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список транзакций по статусу.

    Args:
        transactions: Список словарей с транзакциями.
        state: Статус для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        Отфильтрованный список транзакций.
    """
    return [t for t in transactions if t.get('state') == state]

def sort_by_date(
    transactions: List[Dict], reverse: bool = True
) -> List[Dict]:
    """
    Сортирует транзакции по дате.

    Args:
        transactions: Список словарей с транзакциями.
        reverse: Если True - сортировка по убыванию (новые сначала),
                 если False - по возрастанию (старые сначала).

    Returns:
        Отсортированный список транзакций.
    """
    def get_date(transaction: Dict) -> datetime:
        date_str = transaction['date']
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            return datetime.min  # Для некорректных дат

    return sorted(
        transactions, key=get_date, reverse=reverse
    )