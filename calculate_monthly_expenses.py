# coding: utf-8

import csv
import re
import sys

def get_numbers(values):
    numbers = [re.search('\d+\.{0,1}\d*,\d+', value).group() for value in values]
    return [number.replace('.','').replace(',','.') for number in numbers]

def get_to_header(csv_file):
    while csv_file.readline() != '\n':
        pass

with open(sys.argv[1]) as f:
    get_to_header(f)
    reader = csv.DictReader(f, delimiter=';')
    expenses, incoming = [], []
    for row in reader:
        if row['Πρόσημο ποσού'] == 'Χ':
            expenses.append(row['Ποσό'])
        elif row['Πρόσημο ποσού'] == 'Π':
            incoming.append(row['Ποσό'])
total_expenses = sum([float(n) for n in get_numbers(expenses)])
total_incoming = sum([float(n) for n in get_numbers(incoming)])


print("Total expenses: {expenses}\nTotal incoming: {incoming}".format(expenses=total_expenses, incoming=total_incoming))
print("The balance is {balance}".format(balance=total_incoming - total_expenses))
