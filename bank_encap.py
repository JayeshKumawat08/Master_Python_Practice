class BankAccount:
    def __init__(self,acc_no, name, initial_deposit):
        self.acc_no = acc_no
        self.name = name
        # encapculation
        self.__balance = initial_deposit


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs.{amount} deposited successfully")
        else:
            print("invalid deposit Amount")

    def withdraw(self,amount):
        if amount > 0 and amount <  self.__balance:
            self.__balance -= amount
            print(f"Rs.{amount} has been withdrawn successfully")
        elif amount > self.__balance:
            print("Insufficient Balance")
        else:
            print("Invalid withdraw amaount")

    def get_balance(self):
        return self.__balance

def run_bank_system():

    accounts = {}
    while True:
        print("1.Create New Account")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Check Balance")
        print("5.Exit")

        choice = input("Enter your choice: ").strip()

        if choice == 1:
            acc_no = input("Enter the New Account Number: ").strip()
            if acc_no in accounts:
                print("Account already exists!")
            else:
                name = input("Enter the Account Name: ").strip()
                initial = float(input("Enter the Initial Deposit Amount: "))

                accounts[acc_no]= BankAccount(acc_no,name,initial)
                print(f"Account Created Successfully {name}")

        elif choice == 2:
            acc_no = input("Enter the Account Number: ").strip()
            if acc_no in accounts:
                amount = float(input("Enter the amount to be Deposited: "))
                accounts[acc_no].deposit(amount)
            else:
                print("Account not found")

        elif choice == '3':
            acc_no = input("Enter the Account Number: ").strip()
            if acc_no in accounts:
                amount =  float(input("Enter the Amount  to be withdrawn: "))
                accounts[acc_no].withdraw(amount)
            else:
                print("Account not found")

        elif choice == '4':
            acc_no = input("Enter the Account Number: ").strip()
            if acc_no in accounts:
                bal = accounts[acc_no].get_balance()
                user_name = accounts[acc_no].name
                print("Available balance for {user_name} is {bal}.")
            else:
                print("Account not found")

        elif choice == '5':
            print("Shutting off  the System!")
            break
        else:
            print("Invalid Choice:")

if __name__ == "__main__":
    run_bank_system()


