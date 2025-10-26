class Bank:

    def __init__(self, balance: list[int]):
        self.bank = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 - 1 > len(self.bank) or account2 - 1 > len(self.bank):
            return False
        if self.bank[account1-1] < money:
            return False
        
        self.bank[account1-1] -= money
        self.bank[account2-1] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if account - 1 > len(self.bank):
            return False
        self.bank[account-1] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account - 1 > len(self.bank):
            return False
        if self.bank[account-1] < money:
            return False
        self.bank[account-1] -= money
        return True
        