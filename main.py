from bank import Bank
from users import Account, User, Admin

abc_bank = Bank("ABC Bank")

def user_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")
    account_type =  input("Enter Your Account Type (Savings / Current): ")        
    user = User(name, email, address, account_type, abc_bank)
    options = ["1. Deposit", "2. Withdraw", "3. Available Balance", "4. Transaction History", "5. Take Loan", "6. Transfer Money", "7. Exit"]
    
    while True:
        print(f"Welcome {name}")
        print("ABC Bank\n\n")
        for option in options:
            print(option)
        
        choice = int(input("Select Option: "))
        
        if choice == 1:
            amount = int(input("Enter Amount to Deposit: "))
            user.deposit(amount)       
        
        elif choice == 2:
            amount = int(input("Enter Amount to Withdraw: "))
            user.withdraw(amount)           
        
        elif choice == 3:
            user.check_available_balance()        
        
        elif choice == 4:
            user.check_transaction_history()      
        
        elif choice == 5:
            amount = int(input("Enter Amount to Take Loan: "))
            user.take_loan(amount)  
        
        elif choice == 6:
            account_no = int(input("Enter Receiver Account No: "))
            amount = int(input("Enter Amount to Transfer: "))
            user.transfer_money(account_no, amount)        
        
        elif choice == 7:
            break
        
        else:
            print("Invalid Option Selected!")
            
def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    designation = input("Enter Your Designation: ")
    admin = Admin(name, email, designation)
    options = ["1. Create New Admin Account", "2. Delete User Account", "3. View ALL User Accounts", "4. View Total Available Balance", "5. View the Total Loan Amount", "6. Manage Loan Feature", "7. Exit"]
    
    while True:
        print(f"Welcome Admin, {name}")
        print("ABC Bank\n\n")
        for option in options:
            print(option)
        
        choice = int(input("Select Option: "))
        
        if choice == 1:
            name = input("Enter Your Name: ")
            email = input("Enter Your Email: ")        
            admin = Account(name, email)
            admin.create_new_admin(abc_bank, admin)
        
        elif choice == 2:
            account_no = int(input("Enter User Account No to Delete: "))
            admin.delete_bank_account(abc_bank, account_no)
        
        elif choice == 3:
            admin.show_all_accounts(abc_bank)
            
        elif choice == 4:
            admin.check_total_available_balance(abc_bank)
            
        elif choice == 5:
            admin.check_total_loan_amount(abc_bank)
            
        elif choice == 6:
            print("1. Turn ON Loan Feature.")
            print("2. Turn OFF Loan Feature.")
            toggle = int(input("Select the option: "))
            admin.manage_loan_feature(abc_bank, toggle)           
            
        elif choice == 7:
            break
            
        else:
            print("Invalid Option Selected!")
            
while True:
    print("Welcome to ABC Bank!!!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    
    choice = int(input("Select An Option: "))
    
    if choice == 1:
        user_menu()
    
    elif choice == 2:
        admin_menu()
    
    elif choice == 3:
        break
    
    else:
        print("Invalid Option")