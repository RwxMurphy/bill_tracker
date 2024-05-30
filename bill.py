import datetime

class Bill:
    def __init__(self, name:str, amount:float, due_date:datetime.date) -> None:
        self.name = name
        self.amount = amount
        self.due_date = due_date

    def __repr__(self) -> str:
        descreption: str = self.name
        return descreption

if __name__ == '__main__':
    # Test bill
    due: datetime.date = datetime.date(2024,6,30)
    phone_bill = Bill('phone', 95.50, due)
    print(phone_bill)

