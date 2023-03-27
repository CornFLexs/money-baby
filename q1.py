import os.path

class BankAccount:
    def __init__(self, name, account_type, balance):
        self.name = name
        self.account_type = account_type
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance - amount < 1000:
            raise ValueError("Minimum balance of 1000/- not maintained")
        self.__balance -= amount
    
    def set_balance(self, balance):
        if balance < 1000:
            raise ValueError("Minimum balance of 1000/- not maintained")
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def to_string(self):
        return f"Name: {self.name}\nAccount Type: {self.account_type}\nBalance: {self.__balance}"
    
def create_account():
    name = input("Enter your name: ")
    account_type = input("Enter account type (saving or current): ")
    balance = int(input("Enter initial balance: "))
    account = BankAccount(name, account_type, balance)
    print(f"Account created for {name} with {account_type} account type and initial balance of {balance}/-.")
    return account
    
def main():
    account_list = []
    filename = "accounts.txt"
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                account_data = line.strip().split(",")
                account = BankAccount(account_data[0], account_data[1], int(account_data[2]))
                account_list.append(account)
        print(f"{len(account_list)} accounts loaded from {filename}.")
    else:
        print(f"{filename} does not exist. Creating new file.")
    
    while True:
        print("\nChoose an option:")
        print("1. Create a new account")
        print("2. Access an existing account")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            account = create_account()
            account_list.append(account)
            with open(filename, "a") as file:
                file.write(f"{account.name},{account.account_type},{account.get_balance()}\n")
                
        elif choice == "2":
            if not account_list:
                print("No accounts found.")
            else:
                name = input("Enter your name: ")
                account_found = False
                
                for account in account_list:
                    if account.name == name:
                        account_found = True
                        while True:
                            print("\nChoose an option:")
                            print("1. Withdraw money")
                            print("2. Deposit money")
                            print("3. Exit")
                            sub_choice = input("Enter your choice (1/2/3): ")
                            if sub_choice == "1":
                                try:
                                    amount = int(input("Enter amount to withdraw: "))
                                    account.withdraw(amount)
                                    with open(filename, "w") as file:
                                        for acc in account_list:
                                            file.write(f"{acc.name},{acc.account_type},{acc.get_balance()}\n")
                                    print(f"{amount} withdrawn from your account. New balance is {account.get_balance()}.")

                                except ValueError as e:
                                    print(e)
                            
                            elif sub_choice == "2":
                                try:
                                    amount = int(input("Enter amount to deposit: "))
                                    account.deposit(amount)
                                    with open(filename, "w") as file:
                                        for acc in account_list:
                                         file.write(f"{acc.name},{acc.account_type},{acc.get_balance()}\n")
                                        print(f"{amount} deposited to your account. New balance is {account.get_balance()}.")

                                except ValueError as e:
                                    print(e)
            
                if not account_found:
                    print(f"No account found with name {name}.")
    
        elif choice == "3":
            break
    
        else:
            print("Invalid choice.")
            print("Exiting program.")
        
        
if __name__ == "__main__":
    main()
