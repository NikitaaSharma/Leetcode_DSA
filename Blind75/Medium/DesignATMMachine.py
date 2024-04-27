class ATM:
    def __init__(self) -> None:
        self.account = [0] * 5
        self.denominations = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        self.account = [a + b for a, b in zip(self.account, banknotesCount)]
        print(self.account)

    def withdraw(self, amount):
        take = [0] * 5
        # iterate over the denominations array in reverse order
        for i in range(4, -1, -1):
            # update the take array of i to have the minimum notes needed to fulfill the amount, minium of available notes and notes needed
            take[i] = min(self.account[i], amount // self.denominations[i])
            # update amount
            amount -= take[i] * self.denominations[i]
        
        if amount == 0:
            self.account = [a - b for a, b in zip(self.account, take)]
        
        return [-1] if amount else take


# Your ATM object will be instantiated and called as such:

obj = ATM()
obj.deposit([0,0,1,2,1])
res = obj.withdraw(600)
print(res)
obj.deposit([0,1,0,1,1])
res = obj.withdraw(600)
print(res)
res = obj.withdraw(550)
print(res)
# param_2 = obj.withdraw(amount) 