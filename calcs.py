#https://docs.python.org/3/library/math.html
from math import pi, sqrt

#import os
from os import system

#https://realpython.com/python-data-classes/
from dataclasses import dataclass

@dataclass
class circle:
    diameter: float = 0.0 #Variable annotations: https://www.python.org/dev/peps/pep-0526/
    name: str = "NULL"

    def diameterInput(self):
        self.diameter = float(input("Input diameter: "))
        #self.name = str("Circle")

    def diameterCalculations(self):
        self.radius = float(self.diameter /2)
        self.area = float(pi * sqrt(self.radius))
        self.circumference = float(2 * pi * self.radius)

        print("Radius ", self.radius)
        print("Area: ", self.area)
        print("Circumference: ", self.circumference)

@dataclass
class rectangle:
    side1: float = 0.0
    side2: float = 0.0
    #name: str = "NULL"
    
    def rectangleInput(self):
        self.side1 = float(input("Input the first side of two: "))
        self.side2 = float(input("Input the first side of two: "))
        self.name = str("Rectangle")