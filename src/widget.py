from src.masks import get_mask_card_number, get_mask_account
from typing import Any
import datetime


def mask_account_card(get_mask_card_number: Any, get_mask_account: Any) -> Any:
    """Функция которая принимает номер карты и номер счета и шифрует их"""
    new_masks_card = get_mask_card_number()
    new_mask_account = get_mask_account()
    return f"'Visa'{new_masks_card} \n'Счет'{new_mask_account}"

def get_date() -> Any:
    """Функция выводит время"""
    now_date = datetime.datetime.now()
    get_current_time = f'{now_date.strftime("%d.%m.%Y")}'
    return get_current_time

