import pytest
from src.widget import mask_account_card, get_data


@pytest.fixture
def card_and_account_data():
    return [
        {"type": "card", "number": "1234567890123456"},
        {"type": "account", "number": "12345678901234567890"},
        {"type": "invalid", "number": "invalid_number"},
        {"type": "card", "number": ""},
        {"type": "account", "number": ""},
    ]


@pytest.fixture
def date_data():
    return ["2023-10-01T12:34:56", "invalid_date", "", "2023-10-01"]


def test_mask_account_card(card_and_account_data):
    assert mask_account_card(card_and_account_data[0]) == "1234 56** **** 3456"
    assert mask_account_card(card_and_account_data[1]) == "**7890"
    assert mask_account_card(card_and_account_data[2]) == "invalid_number"
    assert mask_account_card(card_and_account_data[3]) == ""
    assert mask_account_card(card_and_account_data[4]) == ""


def test_get_data(date_data):
    assert get_data(date_data[0]) == "01.10.2023"
    assert get_data(date_data[1]) == "invalid_date"
    assert get_data(date_data[2]) == ""
    assert get_data(date_data[3]) == "01.10.2023"
