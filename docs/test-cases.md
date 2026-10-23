# Test-case table

Function: `calculate_budget(income, expenses)`. Inputs are whole UGX totals for the same period.

Actual results below were obtained by calling the final function. Each row also maps to a
separate pytest test whose name begins with its case ID. The final JUnit XML records all 22 as passed.

| Test Case ID | Category | Input `(income, expenses)` | Expected Result | Actual Result (final) | Status |
| --- | --- | --- | --- | --- | --- |
| TC01 | Normal / surplus | `(500000, 350000)` | `{'balance': 150000, 'status': 'surplus'}` | `{'balance': 150000, 'status': 'surplus'}` | PASS |
| TC02 | Normal / deficit | `(300000, 450000)` | `{'balance': -150000, 'status': 'deficit'}` | `{'balance': -150000, 'status': 'deficit'}` | PASS |
| TC03 | Alternative output / balanced | `(200000, 200000)` | `{'balance': 0, 'status': 'balanced'}` | `{'balance': 0, 'status': 'balanced'}` | PASS |
| TC04 | Boundary / both zero | `(0, 0)` | `{'balance': 0, 'status': 'balanced'}` | `{'balance': 0, 'status': 'balanced'}` | PASS |
| TC05 | Boundary / zero expenses | `(50000, 0)` | `{'balance': 50000, 'status': 'surplus'}` | `{'balance': 50000, 'status': 'surplus'}` | PASS |
| TC06 | Boundary / zero income | `(0, 50000)` | `{'balance': -50000, 'status': 'deficit'}` | `{'balance': -50000, 'status': 'deficit'}` | PASS |
| TC07 | Boundary / balance +1 | `(101, 100)` | `{'balance': 1, 'status': 'surplus'}` | `{'balance': 1, 'status': 'surplus'}` | PASS |
| TC08 | Boundary / balance -1 | `(100, 101)` | `{'balance': -1, 'status': 'deficit'}` | `{'balance': -1, 'status': 'deficit'}` | PASS |
| TC09 | Boundary / balance zero | `(1, 1)` | `{'balance': 0, 'status': 'balanced'}` | `{'balance': 0, 'status': 'balanced'}` | PASS |
| TC10 | Large valid amounts | `(100000000000000000000, 99999999999999999999)` | `{'balance': 1, 'status': 'surplus'}` | `{'balance': 1, 'status': 'surplus'}` | PASS |
| TC11 | Invalid / negative income | `(-1, 100)` | `ValueError: income must not be negative` | `ValueError: income must not be negative` | PASS |
| TC12 | Invalid / negative expenses | `(100, -1)` | `ValueError: expenses must not be negative` | `ValueError: expenses must not be negative` | PASS |
| TC13 | Invalid / text income | `('500000', 100)` | `TypeError: income must be a whole number of UGX` | `TypeError: income must be a whole number of UGX` | PASS |
| TC14 | Invalid / text expenses | `(100, '50')` | `TypeError: expenses must be a whole number of UGX` | `TypeError: expenses must be a whole number of UGX` | PASS |
| TC15 | Invalid / fractional income | `(100.5, 50)` | `TypeError: income must be a whole number of UGX` | `TypeError: income must be a whole number of UGX` | PASS |
| TC16 | Invalid / fractional expenses | `(100, 50.5)` | `TypeError: expenses must be a whole number of UGX` | `TypeError: expenses must be a whole number of UGX` | PASS |
| TC17 | Invalid / boolean income | `(True, 0)` | `TypeError: income must be a whole number of UGX` | `TypeError: income must be a whole number of UGX` | PASS |
| TC18 | Invalid / boolean expenses | `(100, False)` | `TypeError: expenses must be a whole number of UGX` | `TypeError: expenses must be a whole number of UGX` | PASS |
| TC19 | Invalid / None income | `(None, 50)` | `TypeError: income must be a whole number of UGX` | `TypeError: income must be a whole number of UGX` | PASS |
| TC20 | Invalid / None expenses | `(100, None)` | `TypeError: expenses must be a whole number of UGX` | `TypeError: expenses must be a whole number of UGX` | PASS |
| TC21 | Invalid / list expenses | `(100, [20, 30])` | `TypeError: expenses must be a whole number of UGX` | `TypeError: expenses must be a whole number of UGX` | PASS |
| TC22 | Invalid / whole-valued float | `(100.0, 50)` | `TypeError: income must be a whole number of UGX` | `TypeError: income must be a whole number of UGX` | PASS |

## Initial demonstration run

The deliberately faulty draft returned `surplus` for zero balance.
TC03, TC04, and TC09 failed; the other 19 cases passed. After changing
`>= 0` to `> 0`, all 22 passed. See [the report](report.md) for the defect record.

An expected exception is the correct result for TC11–TC22. These cases pass when the
specified error class and exact message are raised.
