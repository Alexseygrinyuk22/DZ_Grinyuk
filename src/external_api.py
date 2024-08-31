import requests
import json

headers= {
  "apikey": "4GDC61W8SwfBY5qlVUmFKUe1IXwCBiW1"
}

def sum_operation_Amount():
    """Функция принимает на вход транзакцию и возвращает сумму транзакций"""
    amount_usd = []  #список в долларах
    amount_eur = []  #список в евро
    amount_rub = []  #список в рублях
    with open(r"../data/operations.json", "r", encoding="utf-8") as file:
        file_json = json.load(file)
        for new_file_json in file_json:
            usd_eur = new_file_json["operationAmount"]['currency']['name']
            if usd_eur == "USD":
                amount_usd.append(new_file_json)

        total_usd = 0  #Сумма транзакций в долларах
        for sum_total in amount_usd:
            x = sum_total['operationAmount'].get('amount', 0)
            total_usd += float(x)
        convent_usd = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=total_usd"
        response = requests.request("GET", convent_usd, headers=headers)
        result_usd = response.text
        result_dict_usd = json.loads(result_usd)
        count_usd = result_dict_usd['result']  #Получение значения конвертации доллара

        for new_file_json in file_json:
            eur_usd = new_file_json["operationAmount"]['currency']['name']
            if eur_usd == "EUR":
                amount_eur.append(new_file_json)

        total_eur = 0  #Сумма транзакций в евро
        for sum_total_eur in amount_eur:
            eur = sum_total_eur['operationAmount'].get('amount', 0)
            total_eur += float(eur)
        convent_eur = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=total_eur"
        response = requests.request("GET", convent_eur, headers=headers)
        result_eur = response.text
        result_dict_eur = json.loads(result_eur)
        count_eur = result_dict_eur['result']  #Получение значения конвертации евро

        for new_file_json in file_json:
            rub = new_file_json["operationAmount"]['currency']['name']
            if rub == "RUB":
                amount_rub.append(new_file_json)

        total_rub = 0  #Сумма транзакций в рублях
        for sum_total in amount_rub:
            rub_ = sum_total['operationAmount'].get('amount', 0)
            total_rub += float(rub_)

        return total_rub + count_eur + count_usd

