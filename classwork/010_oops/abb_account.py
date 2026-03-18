from abc import ABC, abstractmethod

class Account(ABC):

    balance = 0 
    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdrow(self,amount):
        pass 

    def get_balance(self):
        print(f"current balance is {self.balance}")

class SavingAccount(Account):
    def deposite(self,amount):
        self.balance +=amount 
    
    def withdrow(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount

class LoanAccount(Account):
    def withdrow(self, amount):
        self.balance += amount  
    def deposite(self, amount):
        if  amount > self.balance:
            extra = amount - self.balance
            print(f"you have to pay more than your loan amount{ extra}")
        else:
            self.balance -= amount

# s = SavingAccount()
# s.deposite(10000)
# # s.get_balance()
# s.withdrow(50000)
# s.get_balance()

l = LoanAccount()
l.withdrow(100000)
l.deposite(50000)
l.get_balance()
