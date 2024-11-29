# Проект виджет банковских операций клиента

## Описание проекта

Данный проект является реализацией виджета для отображения информации об операциях клиента в банке. В рамках этого проекта были разработаны две основные функции: `filter_by_state` и `sort_by_date`, которые предназначены для фильтрации операций по их состоянию и сортировки их по дате соответственно.

## Установка

Для того чтобы начать использовать данный проект, вам необходимо выполнить следующие шаги:

1. Склонировать репозиторий с помощью команды:

git clone <URL репозитория>

2. Перейти в директорию проекта:

cd project_name


## Использование

В проекте представлены два основных функционала: фильтрация операций по состоянию и сортировка операций по дате.

### Фильтрация операций по состоянию

Функция `filter_by_state` позволяет фильтровать список транзакций по заданному состоянию. По умолчанию, если состояние не указано, будет использоваться значение 'EXECUTED'.

Пример использования функции:

data = [{'id': 1, 'state': 'EXECUTED', 'date': '2022-01-01'}, {'id': 2, 'state': 'CANCELED', 'date': '2022-01-02'}]
filtered_data = filter_by_state(data)
print(filtered_data)  # [{'id': 1, 'state': 'EXECUTED', 'date': '2022-01-01'}]

filtered_data = filter_by_state(data, state='CANCELED')
print(filtered_data)  # [{'id': 2, 'state': 'CANCELED', 'date': '2022-01-02'}]


### Сортировка операций по дате

Функция `sort_by_date` позволяет сортировать список транзакций по дате. По умолчанию, если порядок не указан, будет использоваться порядок убывания.

Пример использования функции:

data = [{'id': 1, 'state': 'EXECUTED', 'date': '2022-01-03'}, {'id': 2, 'state': 'CANCELED', 'date': '2022-01-02'}]
sorted_data = sort_by_date(data)
print(sorted_data)  # [{'id': 2, 'state': 'CANCELED', 'date': '2022-01-02'}, {'id': 1, 'state': 'EXECUTED', 'date': '2022-01-03'}]

sorted_data = sort_by_date(data, descending=False)
print(sorted_data)  # [{'id': 1, 'state': 'EXECUTED', 'date': '2022-01-03'}, {'id': 2, 'state': 'CANCELED', 'date': '2022-01-02'}]

## Модуль `generators`

Модуль `generators` содержит функции для работы с массивами транзакций.

### Функции

- **filter_by_currency**: Фильтрует транзакции по заданной валюте.
  usd_transactions = filter_by_currency(transactions, "USD")
- 
  for _ in range(2):
      print(next(usd_transactions))
- 
**transaction_descriptions**: Возвращает описание каждой операции по очереди.
descriptions = transaction_descriptions(transactions)

 for _ in range(5):
    print(next(descriptions))

**card_number_generator**: Генерирует номера банковских карт в заданном диапазоне.

 for card_number in card_number_generator(1, 5):
    print(card_number)
