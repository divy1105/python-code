
#! Abstraction:

#* Abstraction is the process of hiding the internal details and showing only the necessary information to the user.
#* It achived by using methods overridding and inheritance.

#! 1.Abstract method:
#*the method which is having only declarationbut no body is called as abstract method.
#* we need to write pass in body of abstract method.
#* abstract method is defined by using abc module of python.

#* To make firdt class as abstract class we need to import abc module and inherit ABC class from abc module.
#* In abstract class , there is no any constructor are present.
#* If we want then we can create but no use.
#* We can't create an object of abstract class.
#* An abstract class can have both concrete and abstract method.

#~ e.g.

#~ from abc import ABC, abstractmethod
#~ class shape(ABC):
#~     @abstractmethod
#~     def area(self):
#~         pass

#! 2. concrete method:
#* the method which is having both declaration as well as their body are called as concrete method.

#~ e.g.

#~ from abc import ABC
#~ class shape(ABC):
#~     def area(self):
#~         print("Area")

#* In a class If even a method is abstract method then that class is abstract class.

#~ program on different assistent

#~ Write a program to achive abstraction.for circle,rectangle and triangle to find area and get input from user.

from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self):
        super().__init__("circle")

    def area(self, r):
        print("Area of circle:", 3.14 * r * r)

class rectangle(shape):
    def __init__(self):
        super().__init__("rectangle")

    def area(self, l, b):
        print("Area of rectangle:", l * b)

class triangle(shape):
    def __init__(self):
        super().__init__("triangle")

    def area(self, b, h):
        print("Area of triangle:", 0.5 * b * h)

shape_type = input("Enter the shape to calculate area: ")
if shape_type == "circle":
    s = circle()
    r = eval(input("Enter the radius: "))
    s.area(r)
elif shape_type == "rectangle":
    s = rectangle()
    l = eval(input("Enter the length: "))
    b = eval(input("Enter the breadth: "))
    s.area(l, b)
elif shape_type == "triangle":
    s = triangle()
    b = eval(input("Enter the base: "))
    h = eval(input("Enter the height: "))
    s.area(b, h)
else:
    print("Invalid input")