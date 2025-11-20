#C=2πr

import math

class Circumference:
    r=0
    pi=3.142

    def circumference_of_circle(self):
        C=2*self.pi*self.r
        print(f"circumference of circle is {C}")

circum=Circumference()
circum.r=int(input("Enter the radius : "))

circum.circumference_of_circle()