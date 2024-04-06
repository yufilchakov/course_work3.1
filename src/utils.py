import json


def load_operations_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as load_file:
        operations = json.load(load_file)
    return operations