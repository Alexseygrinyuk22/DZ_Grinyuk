from typing import Any


def get_mask_card_number(card_: Any) -> Any:
    """Функция которая шифрует номер банкосвкой карты"""
    name_card = [item.strip() for item in card_.split(" ")]
    if len(name_card) >= 3:
        name_card = " ".join(name_card[:2])
    else:
        name_card = " ".join(name_card[:1])
    card_number = card_.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    from_card = "".join([private_number[i : i + chunk_size] for i in range(0, chunks, chunk_size)])
    return f"{name_card} {from_card}"


def get_mask_account(bank_account: Any) -> Any:
    """Функция которая шифрует номер банковского счета"""
    number_account = [number.strip() for number in bank_account.split(" ")]
    if len(number_account) >= 3:
        number_account = " ".join(number_account[:2])
    else:
        number_account = " ".join(number_account[:1])
    last_account = bank_account.split()[-1]
    private_last_account = (len(last_account[14:-4]) * "*") + last_account[-4:]
    chunks, chunk_size = len(private_last_account), len(private_last_account)
    from_account = "".join([private_last_account[i : i + chunk_size] for i in range(0, chunks, chunk_size)])
    return f"{number_account} {from_account}"


card_ = "Visa Classic 6831982476737658"
bank_account = "Счет 73654108430135874305"
