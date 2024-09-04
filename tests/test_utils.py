import pytest
from src.utils import financial_transactions


def test_financial_transactions(description=None):
    assert next(financial_transactions(description=None)) == ["Перевод организации"]
