# Brief assignment report

**Student:** Aaine Barintuma  
**Scenario:** Personal Budget Balance  
**Language/framework:** Python and pytest  
**Recorded test date:** 23 October 2026

## 1. Objective

Implement and test one function that subtracts total expenses from total
income, returns the remaining balance, and classifies it as surplus,
balanced, or deficit.

## 2. Inputs, processing, outputs, and validation

| Item | Specification |
| --- | --- |
| Function | `calculate_budget(income, expenses)` |
| Income | Non-negative integer, in whole UGX |
| Expenses | Non-negative integer total, in whole UGX |
| Processing | Validate income, validate expenses, calculate `income - expenses`, classify the balance |
| Positive result | `{"balance": amount, "status": "surplus"}` |
| Zero result | `{"balance": 0, "status": "balanced"}` |
| Negative result | `{"balance": amount, "status": "deficit"}` |
| Incorrect type | Raise `TypeError` naming the input |
| Negative amount | Raise `ValueError` naming the input |

For example, income of 500,000 UGX and expenses of 350,000 UGX produce
`{"balance": 150000, "status": "surplus"}`. A deficit retains its negative
balance so the caller can see how much the expenses exceed income.

### Assumptions

Both totals refer to the same period and currency. Expenses are supplied as
one total; the function does not sum a list. Amounts use whole Uganda
shillings. Fractional amounts and floats such as `100.0` are outside this
interface. This avoids floating-point money calculations and keeps the
exercise small. There is no specified maximum amount, so Python integers
are accepted without an application limit, subject to available resources.

The caller must provide both arguments. The function does not convert text
to numbers, round amounts, store data, print results, or interactively ask
for input. If both inputs are invalid, income is checked first. Python
booleans are rejected explicitly because `bool` is a subclass of `int`.

## 3. Test design

There are **22 separate pytest test functions**, each linked to one row in
[the test-case table](test-cases.md). Expected results are written directly
in the tests instead of being calculated using the function's own logic.

| Coverage | Cases | Purpose |
| --- | --- | --- |
| Normal inputs and alternative outputs | TC01–TC03 | Exercise surplus, deficit, and balanced outcomes |
| Zero and balance boundaries | TC04–TC09 | Check zero totals and balances immediately above, at, and below zero |
| Large valid integers | TC10 | Check exact subtraction of large amounts |
| Negative amounts | TC11–TC12 | Check `ValueError` and its message |
| Wrong types | TC13–TC22 | Check `TypeError` and its message for each supported rejection example |

`assert` compares the complete returned dictionary with the expected
dictionary. `pytest.raises` checks the error class and message. An invalid
input test passes when the expected error is raised; it does not mean the
invalid input was accepted.

## 4. Execution results

The tests were executed with Python 3.12.14 and pytest 8.3.5 on Linux.

| Version | Executed | Passed | Failed | Pytest exit code |
| --- | ---: | ---: | ---: | ---: |
| Deliberately faulty teaching draft | 22 | 19 | 3 | 1 |
| Corrected final function | 22 | 22 | 0 | 0 |

The runs used `python -m pytest -v --color=no` with the corresponding
`--junitxml=evidence/initial-results.xml` or
`--junitxml=evidence/final-results.xml` option. The executable and working
directory are visible in the raw logs. The screenshots show report views
rendering those unedited logs; they are not generated illustrations or
screenshots of a terminal application.

## 5. Defect demonstration and correction

**D01 — zero balance classified as surplus.** A deliberately faulty initial
draft used `if balance >= 0`. This included zero in the surplus branch and
made the following `elif balance == 0` branch unreachable.

| Evidence | Details |
| --- | --- |
| Failing cases | TC03, TC04, TC09 |
| Example input | Income `200000`, expenses `200000` |
| Expected | `{"balance": 0, "status": "balanced"}` |
| Initial actual result | `{"balance": 0, "status": "surplus"}` |
| Correction | Change `if balance >= 0` to `if balance > 0` |
| Retest | All three cases passed; all 22 tests passed |

The initial source is preserved in `evidence/initial-budget.py.txt`. This
was a seeded teaching defect, not an assertion that a real user reported
the bug. No other defects were observed in this test suite. Re-running
all tests after the correction checked that the existing surplus, deficit,
and validation behavior still worked. This is regression testing.

## 6. Submission checklist and limitations

| Assignment task | Submitted evidence |
| --- | --- |
| Test-case design — 20 marks | `docs/test-cases.md`: 22 inputs, expected results, actual results, statuses |
| Function implementation — 20 marks | `budget.py`: one function with validation and all three outcomes |
| Automated testing — 35 marks | `test_budget.py`: 22 pytest tests |
| Execution/reporting — 15 marks | Initial/final raw logs, XML, HTML, PNG screenshots, and this defect report |
| Submission/presentation — 10 marks | README and `docs/explanation.md`, plus source, tests, table, report, and screenshots |

The final function passed all 22 tests under the stated assumptions. This
does not prove correctness for every possible input. Decimal money, lists
of expenses, multiple currencies, and a full application are outside the
chosen scope. The student should understand, run, and explain the solution
and follow the institution's rules on acknowledging assistance.
