import re
from typing import Dict, List


def search_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Поиск транзакций по описанию с использованием регулярных выражений.

    :param transactions: Список с транзакциями.
    :param search_string: Строка для поиска.
    :return: Список с транзакциями, содержащими search_string в описании.
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


from collections import Counter


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict:
    """
    Подсчет количества банковских операций определенного типа.

    :param transactions: Список с транзакциями.
    :param categories: Список категорий.
    :return: Словарь с количеством операций в каждой категории.
    """
    category_counts = Counter()
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category in description:
                category_counts[category] += 1
    return dict(category_counts)
