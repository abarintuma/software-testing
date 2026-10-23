# Personal Budget Balance — Python and pytest

Software Testing Practical Assignment · Aaine Barintuma

One function calculates how much money remains after expenses and returns
`surplus`, `balanced`, or `deficit`. There is no database or web application.

## Start here

1. Read [budget.py](budget.py), the function being tested.
2. Read [test_budget.py](test_budget.py), with 22 individually named tests.
3. See [the test-case table](docs/test-cases.md) for inputs and actual results.
4. Read [the brief report](docs/report.md) and [the explanation guide](docs/explanation.md).
5. Open [the final test screenshot](evidence/final-results.png).

## Set up and run

Install Python 3.10 or later, then open a terminal in this repository:

```sh
python -m venv .venv
```

Activate it on Linux or macOS:

```sh
source .venv/bin/activate
```

Or on Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Install pytest and run the tests:

```sh
python -m pip install -r requirements.txt
python -m pytest -v
```

If your computer uses `python3`, use that command instead of `python` when
creating the virtual environment. The recorded final run had **22 passed,
0 failed**. Your execution time and paths will differ.

Run just one test:

```sh
python -m pytest -v test_budget.py::test_TC07_one_shilling_surplus
```

## Try the function

Start Python with `python`, then enter:

```python
from budget import calculate_budget

calculate_budget(500_000, 350_000)
# {'balance': 150000, 'status': 'surplus'}

calculate_budget(200_000, 200_000)
# {'balance': 0, 'status': 'balanced'}

calculate_budget(300_000, 450_000)
# {'balance': -150000, 'status': 'deficit'}
```

Underscores make numbers easier to read: `500_000` equals `500000`.
Use `exit()` to leave Python.

## Rules and assumptions

- `income` and `expenses` are totals for the **same period**, such as one month.
- Both are non-negative integers in **whole Uganda shillings (UGX)**.
- `expenses` is one total, not a list of purchases.
- Decimal amounts, including `100.0`, are rejected by this integer-only interface.
- Strings, booleans, `None`, lists, and other non-integer inputs raise `TypeError`.
- Negative integers raise `ValueError`. Zero is valid.
- Expenses may exceed income; that is a valid deficit.
- A positive balance means `surplus`; zero means `balanced`; negative means `deficit`.

These are stated assumptions because the assignment does not specify the
currency, decimal handling, or whether expenses should be a list.

## Evidence

| Run | Passed | Failed | Evidence |
| --- | ---: | ---: | --- |
| Deliberately faulty teaching draft | 19 | 3 | [Screenshot](evidence/initial-results.png), [raw log](evidence/initial-pytest.txt) |
| Corrected final function | 22 | 0 | [Screenshot](evidence/final-results.png), [raw log](evidence/final-pytest.txt) |

The PNGs are screenshots of rendered reports containing the unedited
pytest console output. The accompanying HTML and JUnit XML are included.
The initial bug was deliberately seeded to demonstrate defect detection;
it is not presented as an accidental historical defect. The exact draft is
preserved in [initial-budget.py.txt](evidence/initial-budget.py.txt).

To record a fresh final result locally:

```sh
python -m pytest -v --junitxml=evidence/my-results.xml
```

You can also run pytest in your own terminal and take a screenshot for your
presentation. Read the explanation guide and practise the examples before
submitting the work individually.
