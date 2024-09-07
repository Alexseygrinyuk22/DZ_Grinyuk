import json


def financial_transactions(description=None):
    """Функция которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    new_list_json = []
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        file_json = json.load(file)
        if file_json == None:
            return [{}]
        else:
            for new_file_json in file_json:
                new_list_json.append(new_file_json["description"])
        yield new_list_json


print(next(financial_transactions()))
print(next(financial_transactions()))
