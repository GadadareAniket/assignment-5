class account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

class savingaccount(account):
    def __init__(self,title=None,balance=0,intrestrate=0):
        super().__init__(title,balance)
        self.intrestrate=intrestrate

    def __str__(self):
        return str(self.title)+" "+str(self.balance)+" "+str(self.intrestrate)

a=savingaccount("ashish",5000,5)
print(a)