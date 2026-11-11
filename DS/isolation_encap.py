class CustomerAccount:
    def __init__(self,name,initial_balance):
        self.name = name
        
        self.purchase_history = []

        self.__balance = initial_balance


    @property
    def balance(self):
        return self.__balance

    
    def make_purchase(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.purchase_history.append(amount)
            return True
        return False

user1 = CustomerAccount("Jayesh",200)
user1.make_purchase(50)

user2 = CustomerAccount("Sogani",100)
user2.make_purchase(20)

print("Jayesh's History:", user1.purchase_history)
print("Sogani's History:", user2.purchase_history)

