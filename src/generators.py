def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """
    Фильтрует транзакции по валюте и возвращает итератор

    :param transactions: Список словарей с транзакциями
    :param currency: Код валюты для фильтрации (например, "USD")
    :return: Итератор по транзакциям в указанной валюте
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> iter:
    """
    Генерирует описания транзакций по очереди

    :param transactions: Список словарей с транзакциями
    :return: Итератор по описаниям транзакций
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> iter:
    """
    Генерирует номера карт в заданном диапазоне

    :param start: Начальный номер (1)
    :param end: Конечный номер (9999_9999_9999_9999)
    :return: Итератор по номерам карт в формате "XXXX XXXX XXXX XXXX"
    """
    for number in range(start, end + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + \
            f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]