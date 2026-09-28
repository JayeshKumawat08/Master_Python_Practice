#method Overloading
# Default Parameter Approach
class Geometry:
    def calculate_area(self, length, width=None):

        if width is None:
            print(f"Area of Square is: {length * length}")
        else:
            print(f"Area of Rectangle is: {length * width}")

math = Geometry()
math.calculate_area(10)
math.calculate_area(10,5)
print()
print('-'*40)

# Variable Argument Approach 
class Shopping:
    def shopping_cart(self, *price):
        total = sum(price)
        print(f"Sum of {len(price)} items i  s: {total}")

cart = Shopping()
cart.shopping_cart(500)    # 1 argument
cart.shopping_cart(100,1000,300,20)      # 4 arguments
print()
print('-')

# practice question 
# Your e-commerce platform needs a payment processor. 
# Depending on the customer, the system might receive just a raw amount, 
# or it might receive an amount plus a discount code.


class PaymentProcessor:
    def process_transaction(self, customer_name, amount, discount_code=None):

        if discount_code is None:
            print(f"{customer_name} your final amount is: {amount}")

        elif discount_code == "STUDENT":
            amount -= amount * (20/100)
            print(f"{customer_name} your final amount after Student discount is: {amount}")

        else:
            print("Invalid Coupon Code.")

bill = PaymentProcessor()
bill.process_transaction("Jayesh",10000)
bill.process_transaction("Sogani",10000,"STUDENT")