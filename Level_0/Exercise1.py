# Solution for Exercise 1.
# Description:
# Create an online banking system with the following features:
#   * Users must be able to log in with a username and password.
#   * If the user enters the wrong credentials three times, the system must lock them out.
#   * The initial balance in the bank account is $2000.
#   * The system must allow users to deposit, withdraw, view, and transfer money.
#   * The system must display a menu for users to perform transactions.
# Author: Rocio Gonzalez Toral 

class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 2000
        self.login_attempts = 0
        self.is_locked = False

    def login(self, entered_username, entered_password):
        if not self.is_locked:
            if entered_username == self.username and entered_password == self.password:
                print("Login successful!")
                self.login_attempts = 0
            else:
                self.login_attempts += 1
                if self.login_attempts == 3:
                    self.lock_account()
                    print("Account locked due to three consecutive login failures.")
                else:
                    print("Invalid credentials. Please try again.")
        else:
            print("Account is locked. Please contact customer support.")

    def lock_account(self):
        self.is_locked = True

    def deposit(self, amount):
        if not self.is_locked:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Account is locked. Unable to perform transactions.")

    def withdraw(self, amount):
        if not self.is_locked:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Account is locked. Unable to perform transactions.")

    def view_balance(self):
        if not self.is_locked:
            print(f"Current balance: ${self.balance}")
        else:
            print("Account is locked. Unable to perform transactions.")

    def transfer(self, target_account, amount):
        if not self.is_locked:
            if self.balance >= amount:
                self.balance -= amount
                target_account.deposit(amount)
                print(f"Transferred ${amount} to {target_account.username}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Account is locked. Unable to perform transactions.")


# Example usage:
user1 = BankAccount("user1", "password123")

# Simulate login attempts
user1.login("user1", "wrong_password")
user1.login("user1", "wrong_password")
user1.login("user1", "wrong_password")  # Account will be locked after this attempt

# Attempting transactions after account is locked
user1.deposit(100)
user1.withdraw(50)
user1.view_balance()

# Creating another account for transfer example
user2 = BankAccount("user2", "securepassword")

# Transferring money between accounts
user1.login("user1", "password123")  # Logging in successfully after unlocking
user1.transfer(user2, 200)
user1.view_balance()
user2.view_balance()

