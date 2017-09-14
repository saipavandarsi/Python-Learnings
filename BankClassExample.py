"""
All bank Operations using methods and loops 
"""
class BankExample:
    """
    init method is used like a constructor
    """
    def __init__(self):
        self.bankDict = {}

    def deposit(self, accountnum, amount):
        if accountnum in self.bankDict:
            self.bankDict[accountnum] = self.bankDict.get(accountnum) + amount
        else:
            self.bankDict[accountnum] = amount

    def withdraw(self, accountnum, amount):
        if accountnum in self.bankDict:
            if amount <= self.bankDict.get(accountnum):
                self.bankDict[accountnum] = self.bankDict.get(accountnum) - amount
            else:
                print "Please try to add money"

        else:
            return "Not Valid Account"

    def showAccounts(self):
        return self.bankDict



_bank = BankExample()
_bank.deposit('shruthi', 500000)
_bank.deposit('shubha', 5000)
_bank.deposit('pavan', 500)
print _bank.showAccounts()
_bank.withdraw('shruthi', 225000)
_bank.withdraw('shubha', 500000)
print _bank.showAccounts()


