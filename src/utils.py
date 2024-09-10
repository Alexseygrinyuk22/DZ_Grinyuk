import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
def read_json_file():
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        operations_json = file.read()
        file_json = json.loads(operations_json)
    return file_json

new_read_json_file = read_json_file()


def financial_transactions(new_read_json_file):
    """Функция которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    new_list_json = []
    if new_read_json_file != new_read_json_file:
            logger.info(f"Не найдены значения о транзакциях {new_read_json_file}")
            return [{}]
    else:
        for new_file_json in new_read_json_file:
            if new_file_json != None:
                logger.info(f"Получение данных файла json{new_read_json_file}")
                new_list_json.append(new_file_json["description"])
                logger.info(f"Получение данных транзакции {new_list_json}")
            return new_list_json


print(financial_transactions(new_read_json_file))

