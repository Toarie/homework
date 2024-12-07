import unittest
from unittest.mock import patch, mock_open
from src.utils import read_json

class TestUtils(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    def test_read_json_empty_file(self, mock_file):
        self.assertEqual(read_json('path/to/file.json'), [])

    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_read_json_not_list(self, mock_file):
        self.assertEqual(read_json('path/to/file.json'), [])

    @patch('builtins.open', new_callable=mock_open, read_data='[{"key": "value"}]')
    def test_read_json_valid(self, mock_file):
        self.assertEqual(read_json('path/to/file.json'), [{"key": "value"}])

if __name__ == '__main__':
    unittest.main()
