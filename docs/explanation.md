# How to understand and present the work

## A short explanation to practise

“My scenario is Personal Budget Balance. I wrote one Python function that
takes total income and total expenses in whole Uganda shillings for the
same period. It validates both values, subtracts expenses from income, and
returns the balance together with surplus, balanced, or deficit status.
I tested it using pytest with 22 cases covering normal inputs, boundaries,
invalid inputs, and expected errors.”

Use your own words and make sure you can demonstrate the examples below.

## Read the function from top to bottom

1. `def calculate_budget(...)` defines the function. `income` and `expenses`
   are its parameters. `: int` and `-> dict` are type hints for readers;
   they do not enforce validation by themselves.
2. The `for` loop validates income and expenses using the same rules.
   `name` holds the input's name, and `amount` holds its value.
3. `isinstance(amount, int)` checks whether the value is an integer.
   The separate boolean check rejects `True` and `False`.
4. `raise TypeError(...)` reports the wrong kind of value.
   `raise ValueError(...)` reports a negative integer. An f-string inserts
   the input's name into the error message.
5. `balance = income - expenses` performs the calculation.
6. `if`, `elif`, and `else` choose one status based on the balance.
7. `return` gives the caller a dictionary containing two named values:
   `balance` and `status`.

Example: `calculate_budget(500_000, 350_000)` validates both numbers,
calculates `150_000`, chooses `surplus`, and returns the dictionary.

## Explain one normal test

```python
def test_TC07_one_shilling_surplus():
    assert calculate_budget(101, 100) == {"balance": 1, "status": "surplus"}
```

- Arrange: choose income `101` and expenses `100`.
- Act: call `calculate_budget(101, 100)`.
- Assert: compare the result with the independently stated expected result.

This checks the smallest positive balance under the whole-shilling
assumption. `==` compares values; `=` assigns a value to a variable.

## Explain an error-handling test

```python
with pytest.raises(ValueError, match="^income must not be negative$"):
    calculate_budget(-1, 100)
```

The context manager expects a `ValueError`. `match` checks its message;
`^` and `$` mean the start and end of the message. If the function accepts
the negative income, raises a different error, or gives a different
message, the test fails.

## Demonstration order

1. Show the two inputs and three possible outputs in the report.
2. Walk through the function with income `500000` and expenses `350000`.
3. Explain one `assert` test and one `pytest.raises` test.
4. Run `python -m pytest -v` and point out the 22 passed tests.
5. Open the initial evidence. Explain that its bug was deliberately seeded:
   `>= 0` wrongly included zero as surplus.
6. Show the corrected `> 0` condition and the final evidence. Explain why
   running the whole suite again helps detect regressions.

## Likely questions

| Question | Answer |
| --- | --- |
| Why pytest? | It discovers `test_` functions, runs assertions, and reports failures clearly. |
| What is a unit test here? | A small automated check of the one budget function, without a database or other services. |
| Why use whole shillings? | It is an explicit simplifying assumption; integer subtraction stays exact. Decimal support would need a revised contract and more tests. |
| Why reject a number in quotes? | `"100"` is text. This function requires the caller to supply an integer. |
| Why reject `100.0`? | It is a float even though its mathematical value is whole. The interface intentionally accepts only integers. |
| Why reject `True`? | Python treats it as integer-like, but a yes/no value is not a valid money amount here. |
| Why allow expenses greater than income? | That is a legitimate deficit outcome, not an invalid input. |
| Why allow zero? | A person can have no income, no expenses, or both. Equal amounts must produce `balanced`. |
| What is a boundary test? | A check near where behavior changes: balances of `-1`, `0`, and `1`, or the minimum input value `0`. |
| Why is an error test marked PASSED? | It passed because the function raised the error that the test expected. |
| Does passing prove there are no bugs? | No. It shows the selected cases passed under the documented assumptions. |
| What is regression testing here? | Re-running all 22 tests after fixing the zero-balance condition to check existing behavior still works. |
