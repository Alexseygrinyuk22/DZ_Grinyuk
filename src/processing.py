from typing import Iterable


def filter_by_state(
    list_of_dictionaries: Iterable[list], state="EXECUTED"
) -> Iterable[list]:
    """Функция которая возращает только словари содержащие staet
    значению Exsecuted"""
    new_list = []
    for state_new in list_of_dictionaries:
        if state_new.get("state") == state:
            new_list.append(state_new)
    return new_list


def sort_by_date(list_dictionaris: Iterable[list], decreasing=False) -> Iterable[list]:
    """Функция для сортировки списка по дате"""
    sorted_date = sorted(list_dictionaris, key=lambda x: x["date"], reverse=decreasing)
    return sorted_date
