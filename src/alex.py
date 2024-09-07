import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_apilayer_token = os.getenv("key_api")
headers = {"apikey": f"token {api_apilayer_token}"}


def sum_operation_Amount():
    """Функция принимает на вход транзакцию и возвращает сумму транзакций"""
    amount_usd = []  # список в долларах
    amount_eur = []  # список в евро
    amount_rub = []  # список в рублях
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        operations_json = file.read()
        file_json = json.loads(operations_json)
        for new_file_json in file_json:
            if new_file_json == None:
                return [{}]
            if new_file_json["operationAmount"]["currency"].get("code") == "USD":
                amount_usd.append(new_file_json)
            elif new_file_json["operationAmount"]["currency"].get("code") == "EUR":
                amount_eur.append(new_file_json)
            else:
                amount_rub.append(new_file_json)
        return amount_usd


print(sum_operation_Amount())
