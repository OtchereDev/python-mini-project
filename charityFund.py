class CharityFund():
    def __init__(self, balance=1000000):
        self.balance=balance
    def save_fund(self, amount):
        self.balance+=amount
    def spend_fund(self, amount):
        self.balance -= amount
   
    def invest(self, return_rate):
        self.balance *= 1 + return_rate
    def get_balance(self):
        if self.balance < 0:
            print("You have a deficit "+ str(-self.balance)+ " in your account")
        return (self.balance)
    def is_danger(self):
        if self.balance < 50000:
            print ("You are in the danger zone")
        return self.balance < 50000

olivers_fund=CharityFund()
olivers_fund.spend_fund(10000)
print(olivers_fund.get_balance())
olivers_fund.invest(-.5)
print(olivers_fund.get_balance())
olivers_fund.save_fund(1000)
print(olivers_fund.get_balance())
print(olivers_fund.is_danger())