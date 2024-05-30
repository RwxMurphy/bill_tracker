import datetime
from bill import Bill

class User:
    def __init__(self, name:str, user_id:int) -> None:
        self.name = name
        self.user_id = user_id
        self.expenses:list[Bill] = []

    def __repr__(self) -> str:
        description: str = f"User: {self.name} Id:{self.user_id}"
        return description
    
    def add_new_bill(self, name, amount:float, due_date) -> None:
        name = Bill(name, amount, due_date)
        if type(name == Bill):
            if name not in self.expenses:
                self.expenses.append(name)

    def list_all_bills(self) -> list[str]:
        bill_names:list[str] = []
        if len(self.expenses) > 0:
            for bill in self.expenses:
                bill_names.append(bill.name)
        return bill_names

    def remove_bill(self, name: str) -> None:
        for bill in self.expenses:
            if bill.name == name:
                self.expenses.remove(bill)

    

# Test the use and bill modules
if __name__ == '__main__':
    # Test user 1
    murphy =  User('Murphy', 123)
    murphy.add_new_bill('phone', 90.50, datetime.date(2024,6,30))
    murphy.add_new_bill('cable', 60, datetime.date(2024,6,25))
    murphy.add_new_bill('rent', 1650.23,datetime.date(2024,6,1))
    print(murphy)
    
    # Print murphy's bills
    bills = murphy.list_all_bills()
    print(bills)
    

    # Test user 2
    mary =  User('Mary', 321)
    mary.add_new_bill('hydro', 90.50, datetime.date(2024,6,30))
    mary.add_new_bill('cable', 60, datetime.date(2024,6,25))
    mary.add_new_bill('rent', 1425.62, datetime.date(2024,6,1))
    print('\n', mary)
    
    # Remove may's cable bill
    mary.remove_bill('cable')
    
    # Print mary's bills
    bills = mary.list_all_bills()
    print(bills)
    