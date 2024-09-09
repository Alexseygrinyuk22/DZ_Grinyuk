import numpy as np
import csv
import pandas as pd


with open(r"../data/transactions.csv", encoding="utf-8") as file:
    file_csv = csv.reader(file, delimiter=";")
    for new_file_csv in file_csv:
        list_file_csv = new_file_csv

file_exel = pd.read_excel(r"../data/transactions_excel.xlsx")


def func_csv(list_file_csv):
    """Функция для считывания финансовых операций из CSV"""
    return list_file_csv


def func_exel(file_exel):
    """Функция для считывания финансовых операций из Excel"""
    return file_exel.loc[:, "amount"]
