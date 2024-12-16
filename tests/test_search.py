import unittest
from src.search import search_transactions_by_description, count_transactions_by_category

class TestSearch(unittest.TestCase):
    def test_search_transactions_by_description(self):
        transactions = [
            {'description': 'Открытие вклада'},
            {'description': 'Перевод с карты на карту'},
            {'description': 'Перевод организации'},
            {'description': 'Перевод со счета на счет'}
        ]
        result = search_transactions_by_description(transactions, 'вклад')
        self.assertEqual(result, [{'description': 'Открытие вклада'}])

    def test_count_transactions_by_category(self):
        transactions = [
            {'description': 'Открытие вклада'},
            {'description': 'Перевод с карты на карту'},
            {'description': 'Перевод организации'},
            {'description': 'Перевод со счета на счет'}
        ]
        categories = ['вклад', 'перевод']
        result = count_transactions_by_category(transactions, categories)
        self.assertEqual(result, {'вклад': 1, 'перевод': 3})

if __name__ == '__main__':
    unittest.main()
