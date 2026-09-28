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