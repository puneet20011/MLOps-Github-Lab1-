import csv
import os

import pytest

from src import calculator


# ---------- Normal cases (parametrized: one test, many inputs) ----------

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (5, 0, 5),
    (-1, 1, 0),
    (-1, -1, -2),
    (1.5, 2.5, 4.0),
])
def test_add(x, y, expected):
    assert calculator.add(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, -1),
    (5, 0, 5),
    (-1, 1, -2),
    (-1, -1, 0),
])
def test_subtract(x, y, expected):
    assert calculator.subtract(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-1, 1, -1),
    (-1, -1, 1),
])
def test_multiply(x, y, expected):
    assert calculator.multiply(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (6, 3, 2),
    (7, 2, 3.5),
    (-8, 2, -4),
    (0, 5, 0),
])
def test_divide(x, y, expected):
    assert calculator.divide(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (4, 0.5, 2),
    (2, -1, 0.5),
])
def test_power(x, y, expected):
    assert calculator.power(x, y) == expected


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 10),      # 5 + (-1) + 6
    (5, 0, 10),      # 5 + 5 + 0
    (-1, 1, -3),     # 0 + (-2) + (-1)
    (-1, -1, -1),    # -2 + 0 + 1
])
def test_combined(x, y, expected):
    assert calculator.combined(x, y) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 2),
    ([10], 10),
    ([-5, 5], 0),
    ([1, 2], 1.5),
])
def test_average(numbers, expected):
    assert calculator.average(numbers) == expected


# ---------- Error cases (the test passes only if the error IS raised) ----------

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


def test_average_empty_list():
    with pytest.raises(ValueError):
        calculator.average([])


@pytest.mark.parametrize("func", [
    calculator.add,
    calculator.subtract,
    calculator.multiply,
    calculator.divide,
    calculator.power,
    calculator.combined,
])
def test_non_number_input(func):
    with pytest.raises(ValueError):
        func("5", 2)


# ---------- Cases loaded from data/test_cases.csv ----------

OPERATIONS = {
    "add": calculator.add,
    "subtract": calculator.subtract,
    "multiply": calculator.multiply,
    "divide": calculator.divide,
    "power": calculator.power,
}

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "test_cases.csv")


def test_cases_from_csv():
    with open(CSV_PATH, newline="") as f:
        for row in csv.DictReader(f):
            func = OPERATIONS[row["operation"]]
            result = func(float(row["x"]), float(row["y"]))
            assert result == pytest.approx(float(row["expected"])), row
