class User:
    def __init__(self, nombre, email):
        self.name = nombre
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance (self):
        print(f"Usuario: {self.name}, Saldo: ${self.account.display_account_info()}")
        return self
    def transfer_money (self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
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
    def display_account_info(self):
        return self.balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


usuario1 = User("Claudia Quintana", "claudia@python.org")

usuario1.make_deposit(200)
usuario1.make_deposit(500)
usuario1.make_deposit(100)
usuario1.make_withdrawal(300)
usuario1.display_user_balance()

