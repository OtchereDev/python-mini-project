'''defining constructors'''

import pandas as pd

def Merg(dict1, dict2, dict3):
    dict4 = {**dict1,**dict2, **dict3}
    for key, value in dict4.items():
        if key in dict1 and key in dict2 and key in dict3:
            dict4[key] = [value, dict1[key], dict2[key]]

    return dict4

class Bank:
    def __init__(self, account_name, savings, checking, business):
        self.account_name = account_name
        self.savings = savings
        self.checking = checking
        self.Business = business

    def details(self):
        list_details = {'name':self.account_name, 'savings':self.savings,
                            'cheking':self.checking, 'business':self.Business}
        return list_details


customer1 = Bank('Calvin Yee', 4388, 1760, 0)
customer2 = Bank('Anna Sweeney', 0, 0, 22100)
customer3 = Bank('Elias Gonzalez', 6333, 451, 12999)

A = customer1.details()
B = customer2.details()
C = customer3.details()

Bank_dict = Merg(A, B, C)
print(Bank_dict)


''' display bank details in readable form'''
print(pd.DataFrame.from_dict(Bank_dict))

