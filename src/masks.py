import logging
import os

# Создаем форматер для логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Создаем логер для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создаем file_handler для записи логов в файл
log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'masks.log')
file_handler = logging.FileHandler(log_file_path, mode='w')
file_handler.setLevel(logging.DEBUG)

# Устанавливаем форматер для file_handler
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)

def another_function():
    try:
        # Ваш код
        logger.info('Функция another_function выполнена успешно')
    except Exception as e:
        logger.error(f'Ошибка в функции another_function: {e}')

def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    Аргументы:
        card_number (str): Номер карты.

    Возвращает:
        str: Маскированный номер карты.
    """
    try:
        if len(card_number) == 16:
            result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            logger.info(f'Номер карты успешно замаскирован: {result}')
            return result
        logger.warning(f'Некорректный номер карты: {card_number}')
        return card_number
    except Exception as e:
        logger.error(f'Ошибка в функции get_mask_card_number: {e}')
        raise

def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета.

    Аргументы:
        account_number (str): Номер счета.

    Возвращает:
        str: Маскированный номер счета.
    """
    try:
        if len(account_number) >= 20:
            result = f"**{account_number[-4:]}"
            logger.info(f'Номер счета успешно замаскирован: {result}')
            return result
        logger.warning(f'Некорректный номер счета: {account_number}')
        return account_number
    except Exception as e:
        logger.error(f'Ошибка в функции get_mask_account: {e}')
        raise
