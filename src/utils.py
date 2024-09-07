import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def financial_transactions(description=None):
    """Функция которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    new_list_json = []
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        operations_json = file.read()
        file_json = json.loads(operations_json)
        if file_json == description:
            logger.info(f"Не найдены значения о транзакциях {file_json}")
            return [{}]
        else:
            for new_file_json in file_json:
                logger.info(f"Получение данных файла json{file_json}")
                new_list_json.append(new_file_json["description"])
                logger.info(f"Получение данных транзакции {new_list_json}")
                yield new_list_json


print(next(financial_transactions()))
