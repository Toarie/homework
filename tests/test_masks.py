import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    return [
        "1234567890123456",  # Стандартный номер карты
        "123456789012345",  # Нестандартная длина
        "",  # Пустая строка
        "invalid_card_number",  # Некорректный номер
    ]


@pytest.fixture
def account_numbers():
    return [
        "12345678901234567890",  # Стандартный номер счета
        "1234567890123456",  # Меньше ожидаемой длины
        "",  # Пустая строка
        "invalid_account_number",  # Некорректный номер
    ]


def test_get_mask_card_number(card_numbers):
    assert get_mask_card_number(card_numbers[0]) == "1234 56** **** 3456"
    assert get_mask_card_number(card_numbers[1]) == "1234 56** **** 345"
    assert get_mask_card_number(card_numbers[2]) == ""
    assert get_mask_card_number(card_numbers[3]) == "invalid_card_number"


def test_get_mask_account(account_numbers):
    assert get_mask_account(account_numbers[0]) == "**7890"
    assert get_mask_account(account_numbers[1]) == "**3456"
    assert get_mask_account(account_numbers[2]) == ""
    assert get_mask_account(account_numbers[3]) == "invalid_account_number"
