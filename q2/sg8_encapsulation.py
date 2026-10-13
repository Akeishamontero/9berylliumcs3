### ACTIVITY 3

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = float(f"{balance:.2f}")
        

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
                return {"Account Number": self.__account_number}
     
    def set_balance(self, balance):
        if balance < 0:
            raise ValueError("Balance must be not be a negative number.")        
        return
        self.__balance = float(f"{balance:.2f}")

    def get_balance(self):
            return self.__balance

    def display_info(self):
        print("Account", 1)
        print("Account Number:", self.__account_number)
        print("Balance:", f"{self.__balance:.2f}")


#Create an instance of BankAccount Object
a1 = BankAccount("12345", 1000)
a1.display_info()

print()
print("Update balance to -100")
a1.set_balance(-100)
print("Account Number:", a1.get_account_number)
print("Balance:", f"{a1.get_balance():.2f}")

