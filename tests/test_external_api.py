import os
from dotenv import load_dotenv
import requests
import json
from unittest.mock import Mock
from unittest.mock import patch
from src.external_api import sum_operation_Amount

load_dotenv()
api_apilayer_token = os.getenv('key_api')
headers = {"apikey": f'token {api_apilayer_token}'}


def test_sum_operation_Amount():
    convent_usd = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    response = requests.request("GET", convent_usd, headers=headers)
    result_usd = response.text
    result_dict_usd = json.loads(result_usd)
    count_usd = result_dict_usd["result"]
    mock_count_usd = Mock(return_value=99)
    count_usd = mock_count_usd
    assert sum_operation_Amount() == 99
    mock_count_usd.assert_called()


def convert_get_api():
    convent_usd = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    response = requests.request("GET", convent_usd, headers=headers)
    return response.text


@patch("requests.get")
def test_convert_get_api():
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1725345975, "rate": 89.755286},
        "date": "2024-09-03",
        "result": 89.755286,
    }
    assert convert_get_api == {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1725345975, "rate": 89.755286},
        "date": "2024-09-03",
        "result": 89.755286,
    }
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1")
