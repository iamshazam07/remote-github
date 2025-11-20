class Triangle:
    base=0
    height=0

    def area_of_triangle(self):
        area=0.5*self.base*self.height
        print(f"{area}, is the area of triangle....")


triangle=Triangle()

triangle.base=int(input("Enter the base value : "))
triangle.height=int(input("Enter the height value : "))

triangle.area_of_triangle()

#area trapezium
#area quadratic equation
#permiter of square
#area of rectangle
#circumference of circle
#------------------------------------
#create a class named vehicle
#objects should be Truck, car, bus

