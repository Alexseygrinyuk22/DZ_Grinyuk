from typing import Iterable
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
def get_mask_card_number(card_: Iterable[list]) -> Iterable[list]:
    """Функция которая шифрует номер банкосвкой карты"""
    name_card = [item.strip() for item in card_.split(" ")]
    logger.info(f" Проверка ввода карты {name_card}")
    if name_card = None:
        logger.info(f"Ввели не правельное значение карты{name_card}")
        return None
    elif len(name_card) >= 3:
        name_card = " ".join(name_card[:2])
    else:
        name_card = " ".join(name_card[:1])
    card_number = card_.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    from_card = "".join(
        [private_number[i : i + chunk_size] for i in range(0, chunks, chunk_size)]
    )
    logger.info(f"Ввод карты{name_card} и ее шифр {from_card}")
    return f"{name_card} {from_card}"


def get_mask_account(bank_account: Iterable[list]) -> Iterable[list]:
    """Функция которая шифрует номер банковского счета"""
    number_account = [number.strip() for number in bank_account.split(" ")]
    logger.info(f" Проверка ввода счета {number_account}")
    if number_account = None:
        logger.info(f"Ввели не правельное значение счета{number_account}")
        return None
    elif len(number_account) >= 3:
        number_account = " ".join(number_account[:2])
    else:
        number_account = " ".join(number_account[:1])
    last_account = bank_account.split()[-1]
    private_last_account = (len(last_account[14:-4]) * "*") + last_account[-4:]
    chunks, chunk_size = len(private_last_account), len(private_last_account)
    from_account = "".join(
        [private_last_account[i : i + chunk_size] for i in range(0, chunks, chunk_size)]
    )
    logger.info(f"Ввод счета{number_account} и ее шифр {from_account}")
    return f"{number_account} {from_account}"


card_ = "Visa Classic 6831982476737658"
bank_account = "Счет 73654108430135874305"
