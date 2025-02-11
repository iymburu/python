from abc import ABC,abstractmethod
from pyclbr import Class


class Account:
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        print(f"Attempting to withdraw {amount} from account {self.account_id} with balance {self.balance}")
        if amount <= self.balance:
          self.balance -= amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.balance
    def get_holder_name(self):
        return self.holder_name
#inheritance
class Customer(Account):
    def __init__(self, account_id, holder_name, balance, phone_number):
        super().__init__(account_id, holder_name, balance)
        self.phone_number = phone_number
#polymorphism
class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        pass
class DepositTransaction(Transaction):
    def execute(self,account):
        account.deposit(self.amount)

class WithdrawTransaction(Transaction):
    def execute(self,account):
        account.withdraw(self.amount)

#Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
class MpesaPaymentSystem(PaymentSystem):
    def process_payment(self, amount):
        print(f"processing Mpesa payment of {amount}")

#example usage
mpesa=MpesaPaymentSystem
Account1=Customer(1,"Ivy",400,"0723456234")
deposit=DepositTransaction(450)
withdraw=WithdrawTransaction(1750)

deposit.execute(Account1)
withdraw.execute(Account1)
print(f"The balance of {Account1} is {Account.get_balance}")