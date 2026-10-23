"""Each test checks one example from docs/test-cases.md.

An assertion checks a returned result. pytest.raises checks that invalid
input produces the expected error instead of a budget result.
"""

import pytest

from budget import calculate_budget


def test_TC01_normal_surplus():
    assert calculate_budget(500_000, 350_000) == {
        "balance": 150_000, "status": "surplus"
    }


def test_TC02_normal_deficit():
    assert calculate_budget(300_000, 450_000) == {
        "balance": -150_000, "status": "deficit"
    }


def test_TC03_equal_income_and_expenses():
    assert calculate_budget(200_000, 200_000) == {
        "balance": 0, "status": "balanced"
    }


def test_TC04_both_amounts_zero():
    assert calculate_budget(0, 0) == {"balance": 0, "status": "balanced"}


def test_TC05_zero_expenses():
    assert calculate_budget(50_000, 0) == {
        "balance": 50_000, "status": "surplus"
    }


def test_TC06_zero_income():
    assert calculate_budget(0, 50_000) == {
        "balance": -50_000, "status": "deficit"
    }


def test_TC07_one_shilling_surplus():
    assert calculate_budget(101, 100) == {"balance": 1, "status": "surplus"}


def test_TC08_one_shilling_deficit():
    assert calculate_budget(100, 101) == {"balance": -1, "status": "deficit"}


def test_TC09_one_shilling_each():
    assert calculate_budget(1, 1) == {"balance": 0, "status": "balanced"}


def test_TC10_large_amounts():
    assert calculate_budget(10**20, 10**20 - 1) == {
        "balance": 1, "status": "surplus"
    }


def test_TC11_negative_income():
    with pytest.raises(ValueError, match="^income must not be negative$"):
        calculate_budget(-1, 100)


def test_TC12_negative_expenses():
    with pytest.raises(ValueError, match="^expenses must not be negative$"):
        calculate_budget(100, -1)


def test_TC13_text_income():
    with pytest.raises(TypeError, match="^income must be a whole number of UGX$"):
        calculate_budget("500000", 100)


def test_TC14_text_expenses():
    with pytest.raises(TypeError, match="^expenses must be a whole number of UGX$"):
        calculate_budget(100, "50")


def test_TC15_fractional_income():
    with pytest.raises(TypeError, match="^income must be a whole number of UGX$"):
        calculate_budget(100.5, 50)


def test_TC16_fractional_expenses():
    with pytest.raises(TypeError, match="^expenses must be a whole number of UGX$"):
        calculate_budget(100, 50.5)


def test_TC17_boolean_income():
    with pytest.raises(TypeError, match="^income must be a whole number of UGX$"):
        calculate_budget(True, 0)


def test_TC18_boolean_expenses():
    with pytest.raises(TypeError, match="^expenses must be a whole number of UGX$"):
        calculate_budget(100, False)


def test_TC19_none_income():
    with pytest.raises(TypeError, match="^income must be a whole number of UGX$"):
        calculate_budget(None, 50)


def test_TC20_none_expenses():
    with pytest.raises(TypeError, match="^expenses must be a whole number of UGX$"):
        calculate_budget(100, None)


def test_TC21_list_expenses():
    with pytest.raises(TypeError, match="^expenses must be a whole number of UGX$"):
        calculate_budget(100, [20, 30])


def test_TC22_float_with_no_fraction():
    with pytest.raises(TypeError, match="^income must be a whole number of UGX$"):
        calculate_budget(100.0, 50)
