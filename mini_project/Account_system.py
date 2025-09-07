class Account:
    def __init__(self, acc, balance):
        self.account = acc
        self.balance = balance

    # debit    
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Rs", amount, "is debited from your account", self.account)    
        print("Current bank balance is", self.balance)

    # credit
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "is credited to your account", self.account)    
        print("Current bank balance is", self.balance)   

    # show balance
    def show_balance(self):
        print("Your bank balance is Rs", self.balance)
        
# create account once
account = int(input("Enter your bank account number : "))
balance = float(input("Enter your balance for the first time : "))
account_holder = Account(account, balance)

# main loop
while True:
    choice = int(input("\nEnter 1 for Check Balance, 2 for Credit, 3 for Debit, 4 to Exit : "))

    if choice == 1:  # check balance
        account_holder.show_balance()
        new_choice = int(input("Do you want any credit or debit operation? (1 = Yes, 0 = No) : "))

        if new_choice == 1:
            ask = int(input("Press 1 for Credit, 2 for Debit : "))
            if ask == 1:
                amount = float(input("Enter how much rupees you want to add : "))
                account_holder.credit(amount)
            elif ask == 2:
                amount = float(input("Enter how much rupees you want to withdraw : "))
                account_holder.debit(amount)
            else:
                print("Invalid option!")
                break
        else:
            print("Thank you for banking with us!")
            break    

    elif choice == 2:  # credit
        amount = float(input("Enter how much rupees you want to add : "))
        account_holder.credit(amount)

    elif choice == 3:  # debit
        amount = float(input("Enter how much rupees you want to withdraw : "))
        account_holder.debit(amount)

    elif choice == 4:  # exit
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please try again.")
