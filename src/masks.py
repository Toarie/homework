# Запрашиваем у пользователя 16-значный номер карты и номер счета
card_num = input("Введите номер вашей 16-значной карты: ")
account_num = input("Введите номер вашего счета: ")


def get_mask_card_number(card_number: str) -> str:
    """
    Функция маскирует номер карты, оставляя видимыми только первые четыре и последние четыре цифры.

    Аргументы:
    card_number (str): Номер карты в виде строки

    Возвращает:
    str: Маскированный номер карты
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Неверный формат номера карты. Он должен быть 16-значным числом.")

    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card


def get_mask_account(account_number: str) -> str:
    """
    Функция маскирует номер счета, оставляя видимыми только последние четыре цифры.

    Аргументы:
    account_number (str): Номер счета в виде строки

    Возвращает:
    str: Маскированный номер счета
    """
    if not account_number.isdigit():
        raise ValueError("Неверный формат номера счета. Он должен быть строкой из цифр.")

    if len(account_number) < 4:
        raise ValueError("Номер счета слишком короткий.")

    masked_account = f"**{account_number[-4:]}"
    return masked_account


try:
    # Получаем маскированные номер карты и номер счета и выводим их на экран
    print("Маскированный номер карты:", get_mask_card_number(card_num))
    print("Маскированный номер счета:", get_mask_account(account_num))
except ValueError as e:
    # Выводим сообщение об ошибке, если введенные данные не соответствуют требуемому формату
    print(e)
