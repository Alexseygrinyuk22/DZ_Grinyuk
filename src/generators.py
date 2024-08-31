def filter_by_currency(transactions, code="USD"):
    """Функция  возвращает итератор, который поочередно выдает транзакции c кодом USD"""
    new_filter_by_currency = []
    for new_transactions in transactions:
        list_transactions = new_transactions["operationAmount"]["currency"]
        if list_transactions.get("code") == code:
            new_filter_by_currency.append(new_transactions)
    yield new_filter_by_currency


new_filter_by_currency = filter_by_currency()

# Принимает список словарей и возращает поочередно показывает все транзакции
transaction_descriptions = [
    new_description["description"] for new_description in transactions
]


# Генератор выдает номера банковских карт
def card_number_generator(new_card=0):
    while new_card <= 9999999999999999:
        a = "".join(["0"] * (16 - len(str(new_card)))) + str(
            new_card
        )  # Добавление 0 к числу
        b = a.split()[-1]  # пребразование словаря в строку
        chunks, chunk_size = len(b), len(b) // 4
        c = " ".join([b[i : i + chunk_size] for i in range(0, chunks, chunk_size)])
        yield c
        new_card += 1


new_card_number_generator = card_number_generator()
