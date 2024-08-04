from src.masks import get_mask_card_number, get_mask_account, card_, bank_account
from typing import Union
import datetime


def mask_account_card(call_number: Union[str, int]) -> Union[str, int]:
    """Функция которая принимает номер карты или номер счета и шифрует их"""
    if len(call_number.split()[-1]) <= 16:
        return get_mask_card_number(card_)
    else:
        return get_mask_account(bank_account)

def get_date() -> Union[str, int]:
    """Функция выводит время"""
    now_date = datetime.datetime.now()
    get_current_time = f'{now_date.strftime("%d.%m.%Y")}'
    return get_current_time
