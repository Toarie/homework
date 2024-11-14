from datetime import datetime  # Переместите импорт сюда


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счета, оставляя видимыми последние 4 цифры.
    """
    # Разделяем строку на тип карты/счета и номер
    type_number = card_info.split(" ")[1]
    # Проверяем, является ли первая цифра нулем (если да, то это счет)
    if type_number[0] == "0":
        return f"Счет ***{type_number[-4:]}"
    else:
        return f"{card_info[:12]} {card_info[12:-4]} **** {card_info[-4:]}"


def get_date(dt_str: str) -> str:
    """
    Преобразует строку даты-времени в формат dd.mm.yyyy.
    """
    dt_obj = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%S.%f')
    return dt_obj.strftime('%d.%m.%Y')
