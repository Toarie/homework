from datetime import datetime
from typing import List, Dict, Any, Optional

def filter_by_state(data: List[Dict[str, Any]], state: Optional[str] = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по ключу 'state'.

    Аргументы:
        data (List[Dict[str, Any]]): Список словарей для фильтрации.
        state (Optional[str]): Значение состояния для фильтрации. По умолчанию 'EXECUTED'.

    Возвращает:
        List[Dict[str, Any]]: Новый список словарей, соответствующих указанному состоянию.
    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.

    Аргументы:
        data (List[Dict[str, Any]]): Список словарей для сортировки.
        descending (bool): Если True, сортирует в порядке убывания. По умолчанию True.

    Возвращает:
        List[Dict[str, Any]]: Новый список словарей, отсортированный по ключу 'date'.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
