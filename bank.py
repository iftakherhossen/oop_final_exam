class Bank:
    def __init__(self, name):
        self.name = name
        self.user_accounts = {}
        self.total_available_balance = 0
        self.given_loan_amount = 0
        self.loan_eligibility = True
        
        for user in self.user_accounts.items():
            self.total_available_balance += user.balance
            
        for user in self.user_accounts.items():
            self.given_loan_amount += user.loan_balance          
        
    def create_new_account(self, user):
        self.user_accounts[user.account_no] = user   
            
    def delete_bank_account(self, account_no):
        user = self.bank.user_accounts[account_no]  
    
    def show_all_accounts(self):
        print("Users in ABC Bank")
        print("Name\tEmail\tAccount No\t Account Type")
        for account_no, user in self.user_accounts.items():
            print(f"{user.name}\t{user.email}\t{account_no}\t{user.account_type}")
            
    def check_available_balance(self):     
        print(f"The Total Available Balance of ABC Bank is {self.total_available_balance} $")
        
    def check_given_loan_amount(self):          
        print(f"The Total Given Loan Amount of ABC Bank is {self.given_loan_amount} $")
        
    def manage_loan_feature(self, toggle):
        if toggle == 1:
            self.loan_eligibility == True
            
        elif toggle == 2:
            self.loan_eligibility == False
            
        else:
            print("Invalid option selected!")