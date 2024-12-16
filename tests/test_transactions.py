import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from src.transactions import read_csv_transactions, read_excel_transactions

class TestTransactions(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_csv_transactions(self, mock_read_csv):
        mock_data = pd.DataFrame([
            {'date': '2023-01-01', 'amount': 100},
            {'date': '2023-01-02', 'amount': 200}
        ])
        mock_read_csv.return_value = mock_data
        result = read_csv_transactions('transactions.csv')
        self.assertEqual(result, [
            {'date': '2023-01-01', 'amount': 100},
            {'date': '2023-01-02', 'amount': 200}
        ])

    @patch('pandas.read_excel')
    def test_read_excel_transactions(self, mock_read_excel):
        mock_data = pd.DataFrame([
            {'date': '2023-01-01', 'amount': 100},
            {'date': '2023-01-02', 'amount': 200}
        ])
        mock_read_excel.return_value = mock_data
        result = read_excel_transactions('transactions_excel.xlsx')
        self.assertEqual(result, [
            {'date': '2023-01-01', 'amount': 100},
            {'date': '2023-01-02', 'amount': 200}
        ])

if __name__ == '__main__':
    unittest.main()
