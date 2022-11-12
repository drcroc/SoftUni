class Account:

    def __init__(self, id_num: int, name: str, balance=0):
        self.id = id_num
        self.name = name
        self.balance = balance

    def credit(self, amount: int):
        self.balance += amount
        return f'{self.balance}'

    def debit(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            return f'{self.balance}'

        return f'Amount exceeded balance'

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'

