class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if transaction_amount + self.balance < 0:
            raise ValueError(f'sorry cannot go in debt!')

        self._transactions.append(transaction_amount)
        return f'New balance: {self.balance}'

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self.handle_transaction(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, obj):
        return self._transactions[obj]

    def __reverse__(self):
        return self._transactions[::-1]

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_acc = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc
