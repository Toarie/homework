def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    Аргументы:
        card_number (str): Номер карты.

    Возвращает:
        str: Маскированный номер карты.
    """
    if len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return card_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета.

    Аргументы:
        account_number (str): Номер счета.

    Возвращает:
        str: Маскированный номер счета.
    """
    if len(account_number) >= 20:
        return f"**{account_number[-4:]}"
    return account_number
