import unittest
from unittest.mock import mock_open, patch

from src.utils import read_json


class TestUtils(unittest.TestCase):
    """
    Тестовый класс для проверки функции чтения JSON из модуля utils.

    Методы:
        test_read_json_empty_file: Проверяет чтение JSON из пустого файла.
        test_read_json_not_list: Проверяет чтение JSON, который не является списком.
        test_read_json_valid: Проверяет чтение корректного JSON.
    """

    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    def test_read_json_empty_file(self, mock_file):
        """
        Проверяет чтение JSON из пустого файла.

        Использует мок-объект для имитации пустого JSON файла.
        """
        self.assertEqual(read_json('path/to/file.json'), [])

    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_read_json_not_list(self, mock_file):
        """
        Проверяет чтение JSON, который не является списком.

        Использует мок-объект для имитации JSON файла, содержащего объект, а не список.
        """
        self.assertEqual(read_json('path/to/file.json'), [])

    @patch('builtins.open', new_callable=mock_open, read_data='[{"key": "value"}]')
    def test_read_json_valid(self, mock_file):
        """
        Проверяет чтение корректного JSON.

        Использует мок-объект для имитации корректного JSON файла, содержащего список объектов.
        """
        self.assertEqual(read_json('path/to/file.json'), [{"key": "value"}])

if __name__ == '__main__':
    unittest.main()
