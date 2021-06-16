class User:
    def __init__(self, nombre, email):
        self.name = nombre
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal (self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance (self):
        return f"Usuario: {self.name}, Saldo: ${self.account_balance}"
    def transfer_money (self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

usuario1 = User("Guido van Rossum", "guido@python.com")
usuario2 = User("Monty Python", "monty@python.com")
usuario3 = User("Claudia Quintana", "claudia@python.com")

#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
usuario1.make_deposit(300)
usuario1.make_deposit(500)
usuario1.make_deposit(300)
usuario1.make_withdrawal(100)
print(usuario1.display_user_balance())



#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
usuario2.make_deposit(2000)
usuario2.make_deposit(100)
usuario2.make_withdrawal(200)
usuario2.make_withdrawal(500)
print(usuario2.display_user_balance())

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
usuario3.make_deposit(3000)
usuario3.make_withdrawal(500)
usuario3.make_withdrawal(200)
usuario3.make_withdrawal(1000)
print(usuario3.display_user_balance())

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios
usuario3.transfer_money(usuario1, 100)
print(usuario3.display_user_balance())
print(usuario1.display_user_balance())

