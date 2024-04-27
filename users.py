from abc import ABC
import random
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%H:%M:%S, %d/%m/%Y")

class Account(ABC):
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_no = self.generate_acc_no()
        self.transaction_history = []
        self.loan_count = 0
        self.loan_balance = 0
        
    def generate_acc_no(self):
        return random.randint(10000, 99999)
    
    
class User(Account):  
    def __init__(self, name, email, address, account_type, bank):
        super().__init__(name, email, address, account_type)        
        self.bank = bank
        self.bank.create_new_account(self)
        
    def generate_acc_no(self):
        return random.randint(10000, 99999)
        
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} $ in {timestamp}")
        print(f"{amount} $ deposited successfully!")
        print(f"Your new balance is {self.balance} $")
        
    def withdraw(self, amount):
        if self.bank.total_available_balance > 0:
            if self.balance >= amount:            
                self.balance -= amount
                self.transaction_history.append(f"Withdrew {amount} $ in {timestamp}")
                print(f"{amount} $ withdrew successfully!")
                print(f"Your new balance is {self.balance} $")
            else:
                print("Your withdrawal amount exceeded!")
        else:
            print("ABC Bank is Bankrupt!!!")
            
    def check_available_balance(self):
        print(f"Welcome, {self.name} A/c No: {self.account_no}")
        print(f"Your account balance is {self.balance} $")
        
    def check_transaction_history(self):
        i = 1
        print(f"Transaction History of {self.name} A/C No {self.account_no}")
        for history in self.transaction_history:
            print(f"{i}. {history}")
            i += 1
     
    def take_loan(self, amount):
        if self.bank.loan_eligibility == True:
            if self.loan_count <= 2:
                self.loan_balance += amount
                self.loan_count += 1
                print(f"Loan of {amount} $ taken successfully!")
            else:
                print("You have exceed the loan limit!")
        else:
            print("ABC Bank is not giving any loan right now!")
      
    def transfer_money(self, account_no, amount):
        if self.bank.total_available_balance > 0:
            if self.balance >= amount:
                if account_no in self.bank.user_accounts:
                    receiver = self.bank.user_accounts[account_no]
                    receiver.balance += amount
                    self.balance -= amount
                                        
                    self.transaction_history.append(f"Transferred {amount} $ to A/C No. {account_no} in {timestamp}")
                    receiver.transaction_history.append(f"Received {amount} $ from account no. {self.account_no} in {timestamp}")                
                else:
                    print("Account doesn't exist!")                
            else:
                print("You have insufficient balance!")                
        else:
            print("ABC Bank is Bankrupt!!!")
    
    
class Admin:   
    def __init__(self, name, email):
        self.name = name
        self.email = email   
                
    def create_new_account(self, bank, user):
        bank.create_new_account(user)
        
    def delete_user_account(self, bank, account_no):
        bank.delete_user_account(account_no)
        
    def show_all_accounts(self, bank):
        bank.show_all_accounts()
        
    def check_total_available_balance(self, bank):
        bank.check_available_balance()
        
    def check_total_loan_amount(self, bank):
        bank.check_given_loan_amount()
    
    def manage_loan_feature(self, bank):
        bank.manage_loan_feature()