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
    

if __name__ == '__main__':
    #test user
    murphy =  User('Murphy', 123, 100)
    print(murphy)