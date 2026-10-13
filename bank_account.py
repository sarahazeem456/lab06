def process_withdrawal(balance, amount):
    if amount <= 0 or amount % 10 != 0:
        return "Invalid Amount"

    if amount > balance:
        return "Insufficient Funds"

    if amount > 1000:
        return "Limit Exceeded"

    return "Success"