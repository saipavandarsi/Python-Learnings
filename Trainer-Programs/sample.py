class BANK:

    def __init__(self):
        self.acc_info = {}
    
    def deposit(self, acc_no, amount):
        if acc_no in self.acc_info:
            self.acc_info[acc_no] += amount
        else:
            self.acc_info[acc_no] = amount
         
    def withdraw(self, acc_no, amount):
        try:
            if amount <= self.acc_info[acc_no]:
                self.acc_info[acc_no] -= amount
            else:
                return "Balance is less than requested amount"
        except KeyError:
            return "Account doesn't exists" 
         
    def display(self, acc_no):
        try:
            return self.acc_info[acc_no]
        except KeyError:
            return "Account doesn't exists"

