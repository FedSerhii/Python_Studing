class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('Your sum should be more than 0!')

    def withdraw_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print('Sum is more than you have!')

    def __str__(self):
        return f'The owner of account: {self.owner}\nCurrent balance: {self.balance}'


account = BankAccount('Fed Serhii')

account.add_balance(1500)
account.withdraw_money(700)

print(account)
