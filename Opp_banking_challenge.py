class Account:
    def __init__(self, id, name):
        self.id=id
        self.name=name
        self._balance=0
    def balance(self):
        print(f"the total amount of balance is {self._balance}")
    def deposite(self, amount):
        self.amount=amount
        self._balance+=amount
        print(f"the balnace is {self._balance}")
        print("Susscefully credited")
    def credit(self, amount):
        if self._balance>=amount:
            self._balance-=amount
            print(f"the balnace is {self._balance}")
            print("Susscefully debited")
        else:
            print("u donot have the sufficient ampunt in ur account")
    def display(self):
        print(f"the uruser id is {self.id}")
        print(f"the uruser name is {self.name}")
        print(f"the uruser balance is {self._balance}")
class SavingAcc(Account):
    def credit(self, amount):
        interest_rate=0.05
        if self._balance>=(amount*interest_rate):
            self._balance-=amount
            print(f"the balnace is {self._balance}")
            print("Susscefully debited")
        else:
            print("u donot have the sufficient ampunt in ur account")
class CurrentAcc(Account):
    def credit(self, amount):
        current_save=100
        if (self._balance+current_save)>=amount:
            self._balance-=amount
            print(f"the balnace is {self._balance}")
            print("Susscefully debited")
        else:
            print("u donot have the sufficient ampunt in ur account")
class Bank:
    def __init__(self, account):
        if account=="saving":
            self.account=SavingAcc
        elif account=="current":
            self.account=CurrentAcc
    def create_account(self, id, name):
        self.account=id, name
        print("account created successfully")
    def display(self):
        self.account.display()
bank=Bank("saving")
bank.create_account(1, "sai")
bank.display()

