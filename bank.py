def deposit(balance, amount):
    return balance + amount

if __name__ == "__main__":
    current_balance = 1000
    current_balance = deposit(current_balance, 500)
    print(f"Final Balance: {current_balance}")
