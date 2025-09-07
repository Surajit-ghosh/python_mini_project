class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount    
        print("Rs.",amount,"was debited from your bank")
        print("total balance =",self.balance)
    def credit(self,amount):
        self.balance+=amount    
        print("Rs.",amount,"was credited to your bank")
        print("total balance =",self.balance)  
    def get_balance(self): #this is not essential
        return self.balance    

acc1=Account(10000,8918636861)
acc1.debit(1000)
acc1.credit(10000)