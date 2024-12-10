import logging
import os

# Создаем форматер для логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Создаем логер для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создаем file_handler для записи логов в файл
log_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs', 'masks.log')
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
