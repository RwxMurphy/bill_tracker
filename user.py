import datetime
from bill import Bill

class User:
    def __init__(self, name:str, user_id:int, acc_balance:float) -> None:
        self.name = name
        self.user_id = user_id
        self.acc_balance = acc_balance
        self.expenses:list[Bill] = []

    def __repr__(self) -> str:
        description: str = f"User name: {self.name} \nID:{self.user_id} \nUser Bills: {self.expenses}"
        return description
    
    def add_new_bill(self, name: str, amount:float, due_date):
        name = Bill(name, amount, due_date)
        if type(name == Bill):
            if name not in self.expenses:
                self.expenses.append(name)


if __name__ == '__main__':
    #test user 1
    murphy =  User('Murphy', 123, 100)
    murphy.add_new_bill('phone', 90.50, datetime.date(2024,6,30))
    murphy.add_new_bill('cable', 60, datetime.date(2024,6,25))
    print(murphy)

    #test user 2
    mary =  User('Mary', 321, 100)
    mary.add_new_bill('Hydro', 90.50, datetime.date(2024,6,30))
    mary.add_new_bill('cable', 60, datetime.date(2024,6,25))
    print(mary)