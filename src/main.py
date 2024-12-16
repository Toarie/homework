# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name: str) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import json

from src.search import count_transactions_by_category, search_transactions_by_description
from src.transactions import read_csv_transactions, read_excel_transactions


def load_transactions(file_type, file_path):
    if file_type == '1':
        return read_csv_transactions(file_path)
    elif file_type == '2':
        return read_excel_transactions(file_path)
    else:
        with open(file_path, 'r') as file:
            return json.load(file)

def filter_transactions_by_status(transactions, status):
    return [transaction for transaction in transactions if transaction.get('state').upper() == status.upper()]

def sort_transactions_by_date(transactions, order):
    return sorted(transactions, key=lambda x: x['date'], reverse=(order.lower() == 'по убыванию'))

def filter_ruble_transactions(transactions):
    return [transaction for transaction in transactions if 'руб' in transaction.get('operationAmount', {}).get('currency', {}).get('name', '')]

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_type = input("Введите номер пункта: ")
    file_path = input("Введите путь к файлу: ")
    transactions = load_transactions(file_type, file_path)

    print("Для обработки выбран файл с транзакциями.")
    status = ''
    while status not in ['EXECUTED', 'CANCELED', 'PENDING']:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ").upper()
        if status not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print("Статус операции недоступен.")

    transactions = filter_transactions_by_status(transactions, status)
    print(f"Операции отфильтрованы по статусу \"{status}\"")

    sort_order = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_order == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        transactions = sort_transactions_by_date(transactions, order)

    ruble_only = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if ruble_only == 'да':
        transactions = filter_ruble_transactions(transactions)

    search_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if search_description == 'да':
        search_string = input("Введите слово для поиска: ")
        transactions = search_transactions_by_description(transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        print(f"{transaction['date']} {transaction['description']}")
        print(f"Счет {transaction['from']} -> {transaction['to']}")
        print(f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")
        print()

if __name__ == "__main__":
    main()
