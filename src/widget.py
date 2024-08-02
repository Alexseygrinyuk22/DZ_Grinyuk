from src.masks import get_mask_card_number, get_mask_account, card_, bank_account
from typing import Union
import datetime


def mask_account_card(get_mask_card_number: Union[str, int], get_mask_account: Union[str, int]) -> Union[str, int]:
    """Функция которая принимает номер карты и номер счета и шифрует их"""
    new_masks_card = get_mask_card_number(card_)
    new_mask_account = get_mask_account(bank_account)
    return f"{new_masks_card} \n{new_mask_account}"


def get_date() -> Union[str, int]:
    """Функция выводит время"""
    now_date = datetime.datetime.now()
    get_current_time = f'{now_date.strftime("%d.%m.%Y")}'
    return get_current_time


print(mask_account_card(get_mask_card_number, get_mask_account))
