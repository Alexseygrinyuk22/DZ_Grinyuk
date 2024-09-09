import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_apilayer_token = os.getenv("key_api")
headers = {"apikey": f"token {api_apilayer_token}"}


def sum_operation_amount_eur():
    """Функция принимает на вход транзакцию и возращет значение в рублях если сумма была в долларах"""
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        operations_json = file.read()
        file_json = json.loads(operations_json)
        for new_file_json in file_json:
            if new_file_json["operationAmount"]["currency"].get("code") == "USD":
                total_usd = 0  # Сумма транзакций в долларах
                usd = new_file_json["operationAmount"].get("amount", 0)
                total_usd += float(usd)
                convent_usd = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=total_usd"
                response = requests.request("GET", convent_usd, headers=headers)
                result_usd = response.text
                result_dict_usd = json.loads(result_usd)
                count_usd = result_dict_usd["result"]  # Получение значения конвертации доллара
        return total_usd

def sum_operations_amount_eur():
    """Функция принимает на вход транзакцию и возращет значение в рублях если сумма была в Евро"""
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        operations_json = file.read()
        file_json = json.loads(operations_json)
        for new_file_json in file_json:
            if new_file_json["operationAmount"]["currency"].get("code") == "EUR":
                total_eur = 0  # Сумма транзакций в евро
                eur = new_file_json["operationAmount"].get("amount", 0)
                total_eur += float(eur)
                convent_eur = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=total_eur"
                response = requests.request("GET", convent_eur, headers=headers)
                result_eur = response.text
                result_dict_eur = json.loads(result_eur)
                count_eur = result_dict_eur["result"]  # Получение значения конвертации евро
        return total_eur


def sum_operations_amount_rub():
    """Получение суммы в рублях"""
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        operations_json = file.read()
        file_json = json.loads(operations_json)
        for new_file_json in file_json:
            if new_file_json["operationAmount"]["currency"].get("code") == "RUB":
                return new_file_json["operationAmount"]["amount"]



print(sum_operations_amount_rub())
