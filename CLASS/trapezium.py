#in this file we will learn how to code and use class to find Area of trapezium
# The area of a trapezium can be calculated using the lengths of two of its parallel sides 
# and 
# the distance (height) between them. The formula to calculate the area (A) of a trapezium using base and height is given as,

# A = ½ (a + b) h where,

# a and b = bases of the trapezium (parallel sides), and,
# h = height (the perpendicular distance between a and b)

class Trapezium:
    base1=0
    base2=0
    height=0

    def area_of_trapezium(self):
        base=self.base1+self.base2
        area=0.5*base*self.height
        print(f"Area of Trapezium is : {area}")


trapezium=Trapezium()
trapezium.base1=int(input("Enter the base1 value : "))
trapezium.base2=int(input("Enter the base2 value : "))
trapezium.height=int(input("Enter the height of trapezium: "))

trapezium.area_of_trapezium()