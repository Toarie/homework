import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def convert_currency(transaction):
    """
    Converts the transaction amount to rubles if the transaction is in USD or EUR.

    :param transaction: Dictionary with transaction data
    :return: Transaction amount in rubles as a float
    """
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency not in ['USD', 'EUR']:
        return amount

    url = 'https://api.apilayer.com/exchangerates_data/latest'
    params = {
        'symbols': 'RUB',
        'base': currency
    }
    headers = {
        'apikey': API_KEY
    }

    response = requests.get(url, headers=headers, params=params)
    rates = response.json().get('rates')

    if not rates:
        return amount

    rub_rate = rates.get('RUB')
    return amount * rub_rate
