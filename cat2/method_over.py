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