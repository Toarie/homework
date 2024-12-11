import json
import logging
import os

# Создаем форматер для логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Создаем логер для модуля utils
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

# Создаем file_handler для записи логов в файл
log_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'utils.log')
file_handler = logging.FileHandler(log_file_path, mode='w')
file_handler.setLevel(logging.DEBUG)

# Устанавливаем форматер для file_handler
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)

def read_json(file_path):
    """
    Reads a JSON file and returns a list of dictionaries with financial transactions.

    :param file_path: Path to the JSON file
    :return: List of dictionaries with financial transactions
    """
    if not os.path.exists(file_path):
        logger.error(f'Файл {file_path} не существует')
        return []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                logger.warning(f'Файл {file_path} не содержит список данных')
                return []
            logger.info(f'Файл {file_path} успешно прочитан')
            return data
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f'Ошибка при чтении файла {file_path}: {e}')
        return []
