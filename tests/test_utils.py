from src.utils import load_operations_json, list_of_operations, sort_date, get_changes_date, get_hide_number
import os
from config import ROOT_DIR
import pytest


operations = [
    {"id": 1, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
    {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
    {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}]

@pytest.fixture
def operations_fixture():
    return operations

test_path = os.path.join(ROOT_DIR, "tests", "test_operations.json")

def test_load_operations_json():
    assert load_operations_json(test_path) == []


def test_list_of_operations(operations_fixture):
    assert len(list_of_operations(operations_fixture)) == 3


def test_sort_date(operations_fixture):
    assert [i["id"] for i in sort_date(operations_fixture)] == [3, 2, 4, 1]

def test_get_changes_date():
    assert get_changes_date("2018-01-01T00:00:00.000000") == "01.01.2018"


def test_get_hide_number():
    assert get_hide_number("Visa Classic 7756673469642839") == "Visa Classic 7756 67** **** 2839"
    assert get_hide_number("Счет 73654108430135874305")  == "Счет **4305"
