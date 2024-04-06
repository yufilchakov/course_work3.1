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


def get_summa(summa):
    return f"{summa["operationAmount"]["amount"]} {summa["operationAmount"]["currency"]["name"]}"


def get_main(number_operations=5):
    sorting = sort_date(list_of_operations(load_operations_json("operations.json")))
    for operation in sorting:
        if number_operations == 0:
            break
        print(get_changes_date(operation["date"]), operation["description"])
        if operation["description"] != "Открытие вклада":
            print(get_hide_number(operation["from"]) + " -> ", end="")
        print(get_hide_number(operation["to"]),"\n" + get_summa(operation),"\n")
        number_operations -= 1