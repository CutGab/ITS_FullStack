# 8. ATM Machine Simulator:

# Create a function that simulates an ATM machine.
# Initialize an account with a starting balance.
# Allow the user to perform transactions such as deposit, withdraw, and check balance.
# Validate transactions against the account balance and available funds.
# Provide appropriate feedback to the user for each transaction.

User: dict = {"Name": "Gabriele",
              "Starting Balance": 9999,
              "Bank Account": 0
              }

def deposit(amount: float):

    if amount > User["Starting Balance"]:
        print("Spiacenti, ammontare superiore ai fondi.")

    else:
        User["Starting Balance"] -= amount
        User["Bank Account"] += amount

def withdraw(amount: float):

    if amount > User["Bank Account"]:
        print("Spiacenti, ammontare superiore ai fondi.")

    else:
        User["Bank Account"] -= amount
        User["Starting Balance"] += amount

def check_balance():
    print(f"Conto bancario: {User["Bank Account"]}")
    print(f"Conto corrente: {User["Starting Balance"]}")

print(User)

deposit(200)

print("")

print(User)

print("")

withdraw(200)

print("")

print(User)

print("")

check_balance()