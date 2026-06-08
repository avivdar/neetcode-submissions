class Account:
    def __init__(self,name,amount):
        self.title = "Balance:"
        self._balance = amount
    
    def display_balance(self) -> None:
        print(f"{self.title} ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()