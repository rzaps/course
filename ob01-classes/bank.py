class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Счет успешно пополнен. Сумма на счете: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы сняли {money}. Остаток на счете: {self.balance}")

    def all_ballance(self):
        print(f"Текущий баланс: {self.balance}")

client = Account(123, 33000)

client.all_ballance()
client.deposit(55000)
client.withdraw(133000)
client.deposit(66000)
client.withdraw(133000)