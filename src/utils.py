import json
from datetime import datetime

def load_operations_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as load_file:
        operations = json.load(load_file)
    return operations


def list_of_operations(operations):
    operations = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', operations))
    return operations


def sort_date(json_operations):
    json_date_time = sorted(json_operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                            reverse=True)
    return json_date_time


def get_changes_date(date):
    object_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(object_date,'%d.%m.%Y')


def get_hide_number(number):
    requisites = number.split()
    if requisites[0] == "Счет":
        return "Счет **" + number[-4:]
    else:
        card_name = " ".join(requisites[:-1])
        return card_name + " " + requisites[-1][:4] + " " + requisites[-1][4:6] + "** **** " + requisites[-1][-4:]