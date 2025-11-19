# # Python Classes and Objects
# # In the last tutorial, we learned about Python OOP. 
# # We know that Python also supports the concept of objects and classes.

# # An object is simply a collection of data (variables) and methods (functions). 
# # Similarly, a class is a blueprint for that object.

# # Before we learn about objects, let's first learn about classes in Python.

# # Python Classes
# # A class is considered a blueprint of objects.

# # We can think of the class as a sketch (prototype) of a house. 
# # It contains all the details about the floors, doors, windows, etc.

# # Based on these descriptions, we build the house; the house is the object.

# # Since many houses can be made from the same description, we can create many objects from a class.


# # Define Python Class
# # We use the class keyword to create a class in Python. For example,

# class ClassName:
#     # class definition
#     pass

# class Bike:
#     name = ""
#     gear = 0

#     #Here,

# class Employee:
#     pass

# class Executive:
#     name=""
#     Gender = 0
#     number= ""

# class Bottle:
#     pass

# class PlasticBottle:
#     name=""
#     name2=""


# #Bike - the name of the class
# #name/gear - variables inside the class with default values "" and 0 respectively


# #Note: The variables inside a class are called attributes.



# #object in python

# # Python Objects
# # An object is called an instance of a class.

# # Suppose Bike is a class then we can create objects like bike1, bike2, etc from the class.

# # Here's the syntax to create an object.

# # objectName = ClassName()

# # bike2=Bike()
# # bike3=Bike()

# # # access class attributes using object

# # # We use the . notation to access the attributes of a class. For example,

# # # modify the name property
# # bike1=Bike()
# # bike1.name = "Mountain Bike"

# # # access the gear property
# # bike1.gear

# # Here, we have used bike1.name 
# # and 
# # bike1.gear to change and access the value of name and gear attributes, respectively.



# class Bike:
#     name=""
#     gear=0
    

# bike1=Bike()
# bike1.name="Pulsar"
# bike1.gear=4

# print(f"{bike1.name},{bike1.gear}")


# # In the above example, we have defined the class named Bike with two attributes: name and gear.

# # We have also created an object bike1 of the class Bike.

# # Finally, we have accessed and modified the properties of an object using the . notation.



# ##########################################

# # Create Multiple Objects of Python Class
# # We can also create multiple objects from a single class. For example,


# # define a class
# class Employee:
#     # define a property
#     employee_id = 0

# # create two objects of the Employee class
# employee1 = Employee()
# employee2 = Employee()

# # access property using employee1
# employee1.employee_id = 1001
# print(f"Employee ID: {employee1.employee_id}")

# # access properties using employee2
# employee2.employee_id = 1002
# print(f"Employee ID: {employee2.employee_id}")




# class Car:
#     name=""
#     Transmission=""
#     Engine=0
#     Colour=""
#     Model=0

# nexa=Car()
# nexa.name="Jimny"
# nexa.Transmission="Manual"
# nexa.Engine=1550
# nexa.Colour="Green"
# nexa.Model=2025

# toyota=Car()
# toyota.name="Innova"
# toyota.Transmission="Manual"
# toyota.Engine=2435
# toyota.Colour="Pearl WHite"
# toyota.Model=2025

# vw=Car()
# vw.name="Polo"
# vw.Transmission="Automatic"
# vw.Engine=1200
# vw.Colour="Blue"
# vw.Model=2014

# print(nexa.name,
#       nexa.Transmission,
#       nexa.Engine,
#       nexa.Model,
#       nexa.Colour)



##############################################
#METHOD


# Python Methods
# We can also define a function inside a Python class. 
# A Python function defined inside a class is called a method.

# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the properties 
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()


# In the above example, we have created a class named Room with:

# Attributes: length and breadth
# Method: calculate_area()
# Here, we have created an object named study_room from the Room class.

# We then used the object to assign values to attributes: length and breadth.

# Notice that we have also used the object to call the method inside the class,

# study_room.calculate_area()
# Here, we have used the . notation to call the method. Finally, the statement inside the method is executed.
