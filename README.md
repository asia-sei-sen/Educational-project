# Банковский транзакционный процессор

## Описание:
Проект предоставляет инструменты для обработки банковских операций, включая:
- Маскировку конфиденциальных данных (номера карт и счетов)
- Форматирование финансовой информации
- Фильтрацию и сортировку транзакций
- Преобразование дат в удобочитаемый формат

## Установка:
1. Клонируйте репозиторий:
git clone https://github.com/ваш-username/ваш-репозиторий.git
cd ваш-репозиторий

2. Установите зависимости:
pip install -r requirements.txt

## Использование:
1. Импортируйте модули:
from src import masks, widget, processing

2. Примеры использования:
# Маскировка данных карты
masked_card = widget.mask_account_card("Visa Platinum 7000792289606361")

# Фильтрация транзакций
executed_transactions = processing.filter_by_state(transactions_list)

# Сортировка по дате
sorted_trans = processing.sort_by_date(transactions_list)

## Тестирование:
Проект включает комплексные тесты для всех модулей. Для запуска:
pytest test/ -v

Примеры тестов:
1. Модуль масок (masks.py):
- Маскировка карт: "1234567890123456" → "1234 56** **** 3456"
- Маскировка счетов: "1234567890" → "**7890"
- Обработка некорректных данных

2. Модуль виджета (widget.py):
- Автоматическое определение типа данных (карта/счет)
- Сохранение названия платежной системы
- Обработка ошибочных форматов

3. Модуль обработки (processing.py):
- Сортировка транзакций по дате (возрастание/убывание)
- Фильтрация выполненных операций
- Обработка транзакций с некорректными датами

Для проверки покрытия:
pytest --cov=src --cov-report=term-missing

# Генератор банковских данных


Проект для генерации тестовых данных банковских операций:

## Функционал
- Генерация номеров карт (`card_number_generator`)
- Фильтрация транзакций по валюте (`filter_by_currency`)
- Получение описаний транзакций (`transaction_descriptions`)

## Установка
```bash
git clone https://github.com/Asia-Eclipse/Educational-project.git
cd Educational-project
pip install -r requirements.txt
```

## Примеры использования
```python
from generators import card_number_generator

# Генерация 5 номеров карт
for card_number in card_number_generator(1, 5):
    print(card_number)
```

## Тестирование
```bash
pytest test/
```

## Авторы:
- ASIA_K <sei_senagon@yahoo.com>111

## Лицензия:
MIT License