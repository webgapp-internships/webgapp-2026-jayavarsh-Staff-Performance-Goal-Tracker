class bankacc:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def getbalance(self):
        return self.__balance
    def setbalance(self,amount):
        if amount >=0:
            self.__balance = amount
s1=bankacc("Jaya",10000)
print(s1.getbalance())
s1.setbalance(11500)
print(s1.getbalance())

