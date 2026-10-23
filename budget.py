"""Calculate a personal budget using whole Uganda shillings (UGX)."""


def calculate_budget(income: int, expenses: int) -> dict:
    """Return the remaining balance and its surplus/balanced/deficit status.

    Both inputs are totals for the same period, in whole UGX.
    Wrong types raise TypeError; negative amounts raise ValueError.
    """
    # Validate before doing any arithmetic. bool is rejected even though
    # Python treats True and False as a kind of integer.
    for name, amount in (("income", income), ("expenses", expenses)):
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError(f"{name} must be a whole number of UGX")
        if amount < 0:
            raise ValueError(f"{name} must not be negative")

    balance = income - expenses

    if balance > 0:
        status = "surplus"
    elif balance == 0:
        status = "balanced"
    else:
        status = "deficit"

    return {"balance": balance, "status": status}
