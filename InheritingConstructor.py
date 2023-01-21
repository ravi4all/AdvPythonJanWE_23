class Account:

    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no
        print("Parent Class Const. Called...")

    def withdraw(self):
        print("Withdraw Limit is 50000")

    def deposit(self):
        print("Deposit Limit is 25000")

    def showDetails(self):
        print("Hello ",self.name)
        print("Acc No :",self.acc_no)


class SavingAccount(Account):

    def __init__(self):
        # Calling Parent Class Constructor
        super(SavingAccount, self).__init__("Ram", 998342134313)
        self.balance = None
        print("SA Class Const. Called...")

    def roi(self):
        print("ROI is 5%")

    def withdraw(self):
        print("Withdraw Limit is 1 Lac")


account = SavingAccount()
account.withdraw()
account.deposit()
account.showDetails()
account.roi()
