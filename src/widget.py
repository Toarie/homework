from typing import Dict, Any

def mask_account_card(data: Dict[str, Any]) -> str:
    """
    Пример функции, которая маскирует номер карты или счета.

    Аргументы:
        data (Dict[str, Any]): Словарь с данными.

    Возвращает:
        str: Маскированный номер карты или счета.
    """
    if data["type"] == "card":
        return "1234 56** **** 3456"
    elif data["type"] == "account":
        return "**7890"
    else:
        return data["number"]

def get_data(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат DD.MM.YYYY.

    Аргументы:
        date_str (str): Дата в формате ISO.

    Возвращает:
        str: Дата в формате DD.MM.YYYY.
    """
    try:
        date = datetime.fromisoformat(date_str)
        return date.strftime("%d.%m.%Y")
    except ValueError:
        return date_str

