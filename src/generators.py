def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency: Код валюты (например, "USD").
    :return: Итератор, возвращающий транзакции в заданной валюте.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Возвращает описание каждой операции по очереди.

    :param transactions: Список словарей с транзакциями.
    :return: Итератор, возвращающий описания транзакций.
    """
    for transaction in transactions:
        yield transaction['description']


def card_number_generator(start, stop):
    """
    Генерирует номера банковских карт в заданном диапазоне.

    :param start: Начальное значение диапазона.
    :param stop: Конечное значение диапазона.
    :return: Итератор, возвращающий номера карт.
    """
    for number in range(start, stop + 1):
        yield f"{number:016}"


