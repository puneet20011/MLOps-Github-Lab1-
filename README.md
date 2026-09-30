# MLOps (IE-7374) – GitHub Lab 1: Calculator with CI

[![Testing with Pytest](https://github.com/puneet20011/MLOps-Github-Lab1-/actions/workflows/pytest_action.yml/badge.svg)](https://github.com/puneet20011/MLOps-Github-Lab1-/actions/workflows/pytest_action.yml)
[![Python Unittests](https://github.com/puneet20011/MLOps-Github-Lab1-/actions/workflows/unittest_action.yml/badge.svg)](https://github.com/puneet20011/MLOps-Github-Lab1-/actions/workflows/unittest_action.yml)

Based on [Github_Labs/Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1) from the course repo. The lab covers a virtual environment, a structured repo, unit tests with **pytest** and **unittest**, and **GitHub Actions** that run those tests on every push.

## My modifications

| Area | Original lab | This repo |
|---|---|---|
| Functions | `fun1`–`fun4` (add, subtract, multiply, combined) | Clearly named `add`, `subtract`, `multiply`, `combined`, plus new **`divide`**, **`power`** and **`average`** |
| Error handling | Type check on some functions | Type check on every function, `ZeroDivisionError` for divide by zero, `ValueError` for averaging an empty list |
| Data | Empty `data/` folder | `data/test_cases.csv`: a table of problems and expected answers that the tests read |
| Pytest | 4 tests with plain asserts | 38 test cases: parametrized tests, error tests with `pytest.raises`, CSV-driven test |
| Unittest | 4 tests | 8 tests, including `assertRaises` error checks |
| CI: pytest | Python 3.8, deprecated `@v2` actions, invalid trigger config | Python 3.10 / 3.11 / 3.12 matrix, `@v4`/`@v5` actions, flake8 lint, coverage with a 90% minimum, test report artifacts |
| CI triggers | Push to `main` | Push, pull requests to `main`, manual run (`workflow_dispatch`) |
| Workflow location | `workflows/` (not picked up by GitHub) | `.github/workflows/` |

## Project structure

```
.
├── .github/workflows/
│   ├── pytest_action.yml     # lint + pytest + coverage on a Python matrix
│   └── unittest_action.yml   # unittest suite
├── data/
│   └── test_cases.csv        # operation, x, y, expected
├── src/
│   └── calculator.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
└── requirements.txt
```

## Running locally

```bash
python3 -m venv lab_01
source lab_01/bin/activate          # Windows: lab_01\Scripts\activate
pip install -r requirements.txt

flake8 src test --max-line-length=100
pytest -v --cov=src --cov-report=term-missing
python -m unittest test.test_unittest -v
```
