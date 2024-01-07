class Account:

    savings_interest = 7.5
    coorportae_interest = 4
    transitory_balance = 0

    def __init__(self, accoutno, password, balance):
        self.account_number = accoutno
        self.password = password
        self.balance = balance

    def withdraw(self, withdraw_amount):
        Account.transitory_balance = int(self.balance) - int(withdraw_amount)
        if self.balance < 0:
            print("Insufficient funds :(")
        else:
            # return Account.transitory_balance
            pass
    
    def deposit(self, deposit_amount):
        Account.transitory_balance = int(self.balance) + int(deposit_amount)
        # return Account.transitory_balance
    
    def check_balance(self):
        return Account.transitory_balance

# To initiate a subclass...
class Savings_account(Account): # this is the way

    def __init__(self, accoutno, password, balance, initial_deposit): # initial deposit is a supid attribute ikr. but just used here for practice
        super().__init__(accoutno,password, balance) # Instead of rewriting the entire code again super() is used to access the main class
        # Account.__init__(attr1, attr2, ..... attrn) is also an another syntax
        self.initial_deposit = initial_deposit
        self.balance = self.initial_deposit + balance

    def savings_interest(self):
        interest_multiplier = int(Account.savings_interest)/100 # accessing class variable from main class
        return self.balance * (1 + round(interest_multiplier,2))

class Coorporate_account(Account):
    def __init__(self, accoutno, password, balance, company_name):
        super().__init__(accoutno, password, balance)
        self.company_name = company_name 

savings_usr_1 = Savings_account(100021, 'test123', 0, 10000)
print(savings_usr_1.savings_interest())
savings_usr_1.deposit(1000)
print(savings_usr_1.check_balance())
savings_usr_1.withdraw(5000)
print(savings_usr_1.check_balance())
