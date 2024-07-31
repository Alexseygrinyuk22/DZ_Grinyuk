from typing import Any


def get_mask_card_number(card_: Any) -> Any:
    """Функция которая шифрует номер банкосвкой карты"""
    card_number = card_.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    return " ".join([private_number[i : i + chunk_size] for i in range(0, chunks, chunk_size)])


def get_mask_account(bank_account: Any) -> Any:
    """Функция которая шифрует номер банковского счета"""
    last_account = bank_account.split()[-1]
    private_last_account = (len(last_account[14:-4]) * "*") + last_account[-4:]
    chunks, chunk_size = len(private_last_account), len(private_last_account)
    return "".join([private_last_account[i : i + chunk_size] for i in range(0, chunks, chunk_size)])

