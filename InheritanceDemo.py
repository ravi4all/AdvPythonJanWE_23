class Account:
    def withdraw(self):
        print("Withdraw Limit is 50000")

    def deposit(self):
        print("Deposit Limit is 25000")


class SavingAccount(Account):
    def roi(self):
        print("ROI is 5%")

    def withdraw(self):
        print("Withdraw Limit is 1 Lac")


class CurrentAccount(Account):
    def od_limit(self):
        print("Over Draft Limit is 1 Lac")

    def deposit(self):
        print("Deposit Limit is 50000")

# Polymorphic Call
def caller(account):
    account.withdraw()
    account.deposit()
    # account.roi()
    # account.od_limit()
    if isinstance(account, SavingAccount):
        account.roi()
    elif isinstance(account, CurrentAccount):
        account.od_limit()


caller(SavingAccount())
caller(CurrentAccount())

# sa = SavingAccount()
# sa.withdraw()
# sa.deposit()
# sa.roi()
#
# ca = CurrentAccount()
# ca.withdraw()
# ca.deposit()
# ca.od_limit()
