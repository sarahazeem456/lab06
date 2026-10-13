# test_bank_account.py
import pytest
from bank_account import process_withdrawal


def test_successful_withdrawal():
    # Valid amount within balance and daily limit
    assert process_withdrawal(500, 100) == "Success"
    assert process_withdrawal(1000, 1000) == "Success"


def test_invalid_amounts():
    # Negative values, zero, or non-multiples of 10
    assert process_withdrawal(500, 0) == "Invalid Amount"
    assert process_withdrawal(500, -50) == "Invalid Amount"
    assert process_withdrawal(500, 25) == "Invalid Amount"


def test_insufficient_funds():
    # Amount exceeds balance
    assert process_withdrawal(200, 300) == "Insufficient Funds"


def test_limit_exceeded():
    # Amount exceeds the $1000 ATM limit
    assert process_withdrawal(5000, 1200) == "Limit Exceeded"