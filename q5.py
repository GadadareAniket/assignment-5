class Account:
  def __init__(self, title=None, balance=0):
    self.title = title
    self.balance = balance
    
  def withdrawal(self, amount):
    self.amount=self.balance-amount

  def deposit(self, amount):
    self.amount=self.balance+amount

  def getBalance(self):
    return self.amount

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
      super().__init__(title, balance)
      self.interestRate = interestRate
    
    def interestAmount(self):
       self.interestRate=self.interestRate*self.balance/100
       self.amount=self.interestRate+self.amount
       return self.interestRate

obj=SavingsAccount("Ashish", 2000, 5)
obj.balance = 2000
obj.deposit(500)
print("The Available Balance  : ",obj.getBalance())
print("The Interest : ",obj.interestAmount())
print("Balance with interest : ",obj.getBalance())