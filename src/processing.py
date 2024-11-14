from typing import List, Dict
from datetime import datetime


def filter_by_state(transactions: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Фильтрует список транзакций по статусу.

    :param transactions: список словарей с данными транзакций
    :param state: статус для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список транзакций
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список транзакций по дате.

    :param transactions: список словарей с данными транзакций
    :param descending: порядок сортировки (по умолчанию убывающий)
    :return: отсортированный список транзакций
    """
    return sorted(transactions, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
