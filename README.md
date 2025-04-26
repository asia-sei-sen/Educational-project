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

## Авторы:
- ASIA_K  <sei_senagon@yahoo.com>

## Лицензия:
MIT License 