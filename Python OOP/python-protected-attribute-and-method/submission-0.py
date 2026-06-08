class Account:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    
    def title(self) -> str:
        return ("Balance:")
    def _balance(self) -> str:
        return (self.amount)

    def display_balance(self) -> None:
        print(f"{self.title()} ${self._balance()}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
