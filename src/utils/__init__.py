import logging
import os

# Создаем форматер для логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Создаем логер для модуля utils
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

# Создаем file_handler для записи логов в файл
log_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs', 'utils.log')
file_handler = logging.FileHandler(log_file_path, mode='w')
file_handler.setLevel(logging.DEBUG)

# Устанавливаем форматер для file_handler
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)

def some_function():
    try:
        # Ваш код
        logger.info('Функция some_function выполнена успешно')
    except Exception as e:
        logger.error(f'Ошибка в функции some_function: {e}')
