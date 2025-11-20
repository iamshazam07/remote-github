#For the area of a rectangle:
#A = a × b

class Rectangle:
    length=0
    breadth=0

    def area_of_rectangle(self):
        A=self.length*self.breadth
        print(f"area of rectangle is {A}")

rectangle=Rectangle()
rectangle.length=int(input("Enter the length : "))
rectangle.breadth=int(input("Enter the breadth : "))

rectangle.area_of_rectangle()