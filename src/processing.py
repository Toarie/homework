from typing import List, Dict, Optional

def filter_by_state(data: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]:
    """Фильтрует список транзакций по заданному состоянию (по умолчанию 'EXECUTED')."""
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортирует список транзакций по дате (по умолчанию в порядке убывания)."""
    return sorted(data, key=lambda x: x['date'], reverse=descending)
