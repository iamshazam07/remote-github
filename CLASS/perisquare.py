#The formula to calculate the perimeter of a square is given as: P = 4 × side.

class Perimeter:
    side=0

    def permiter_of_square(self):
        P=4*self.side
        print(f"perimiter of square is : {P}")

perimeter=Perimeter()

perimeter.side=int(input("Enter the value of side : "))

perimeter.permiter_of_square()