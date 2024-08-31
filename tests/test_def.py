import pytest

from masks import get_mask_account, get_mask_card_number
from processing import filter_by_state, sort_by_date
from widget import get_date, mask_account_card
from generators import new_filter_by_currency, transaction_descriptions, new_card_number_generator


@pytest.mark.parametrize(
    "get_mask_card_number, card_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("", ""),
    ],
)
def test_get_mask_card_number(get_mask_card_number, card_result):
    assert test_get_mask_card_number(get_mask_card_number) == card_result


def test_get_mask_account(get_mask_account, bank_account_result):
    assert test_get_mask_account(get_mask_account) == bank_account_result


@pytest.mark.parametrize(
    "call_number, call_number_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("", ""),
    ],
)
def test_mask_account_card(mask_account_card, call_number_result):
    assert mask_account_card(mask_account_card) == call_number_result


def test_get_date(get_current_time, result_get_current_time):
    assert get_date(get_current_time) == result_get_current_time


def test_filter_by_state(list_of_dictionaries, new_list):
    assert test_filter_by_state(list_of_dictionaries) == new_list


def test_sort_by_date(list_dictionaris, result_list_dictionaris):
    assert test_sort_by_date(list_dictionaris) == result_list_dictionaris


@pytest.fixture
def my_fixture():
    return None
def test_fixture(my_fixture):
    assert none_fixture(my_fixture) == None
def test_fixture_emty():
    assert none_fixture([]) == []


def test_new_filter_by_currency(filter_by_currency):
    assert next(new_filter_by_currency) == filter_by_currency


def test_transaction_descriptions(new_description):
    assert next(transaction_descriptions) == new_description['description']


def test_new_card_number_generator():
    assert next(new_card_number_generator) == 0000 0000 0000 0000
    assert next(new_card_number_generator) == 0000 0000 0000 0001
    assert next(new_card_number_generator) == 0000 0000 0000 0002