import unittest
from unittest.mock import patch
from src.external_api import convert_currency

class TestExternalApi(unittest.TestCase):
    """
    Тестовый класс для проверки функции конвертации валют из модуля external_api.

    Методы:
        test_convert_currency_usd: Проверяет конвертацию валюты из USD в RUB.
        test_convert_currency_eur: Проверяет конвертацию валюты из EUR в RUB.
        test_convert_currency_rub: Проверяет конвертацию валюты из RUB в RUB.
    """

    @patch('src.external_api.requests.get')
    def test_convert_currency_usd(self, mock_get):
        """
        Проверяет конвертацию валюты из USD в RUB.

        Использует мок-объект для имитации ответа от внешнего API.
        """
        mock_get.return_value.json.return_value = {'rates': {'RUB': 75}}
        transaction = {'amount': 100, 'currency': 'USD'}
        self.assertEqual(convert_currency(transaction), 7500.0)

    @patch('src.external_api.requests.get')
    def test_convert_currency_eur(self, mock_get):
        """
        Проверяет конвертацию валюты из EUR в RUB.

        Использует мок-объект для имитации ответа от внешнего API.
        """
        mock_get.return_value.json.return_value = {'rates': {'RUB': 85}}
        transaction = {'amount': 100, 'currency': 'EUR'}
        self.assertEqual(convert_currency(transaction), 8500.0)

    def test_convert_currency_rub(self):
        """
        Проверяет конвертацию валюты из RUB в RUB.

        В данном случае сумма должна остаться неизменной.
        """
        transaction = {'amount': 100, 'currency': 'RUB'}
        self.assertEqual(convert_currency(transaction), 100)

if __name__ == '__main__':
    unittest.main()
