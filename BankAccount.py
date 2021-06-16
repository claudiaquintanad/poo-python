class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Fondos insuficientes: cobrar una tarifa de ${amount - self.balance}")
        else:
            self.balance -= amount
        return self
    def display_account_infocopy(self):
        print(f"Saldo: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

cuenta1 = BankAccount(0.01)
cuenta2 = BankAccount(0.01)

cuenta1.deposit(200).deposit(200).deposit(200).withdraw(100).yield_interest().display_account_infocopy()
#probando condición cuando se desea hacer un retiro superior al saldo de la cuenta
#cuenta1.withdraw(600)
cuenta2.deposit(1000).deposit(1000).withdraw(300).withdraw(200).withdraw(500).yield_interest().display_account_infocopy()