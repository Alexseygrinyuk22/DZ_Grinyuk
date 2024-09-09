import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_apilayer_token = os.getenv("key_api")
headers = {"apikey": "4GDC61W8SwfBY5qlVUmFKUe1IXwCBiW1"}


def sum_operation_Amount():
    """Функция принимает на вход транзакцию и возвращает сумму транзакций"""
    convent_eur = (
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1"
    )
    response = requests.request("GET", convent_eur, headers=headers)
    result_eur = response.text
    result_dict_eur = json.loads(result_eur)
    one_eur = result_dict_eur["result"]
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        operations_json = file.read()
        file_json = json.loads(operations_json)
    for new_file_json in file_json:
        if new_file_json["operationAmount"]["currency"].get("code") != "RUB":
            amount_eur = new_file_json["operationAmount"]["amount"]
    return float(amount_eur * one_eur)


print(sum_operation_Amount())
