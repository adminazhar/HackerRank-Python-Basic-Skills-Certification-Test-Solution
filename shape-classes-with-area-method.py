#!/bin/python3

import math
import os
import random
import re
import sys

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius * self.radius
    
if __name__ == '__main__':  
# Example usage of the classes (testing)
    
    # Example 1: Rectangle with length 4 and width 5
    rect = Rectangle(4, 5)
    print("{:.2f}".format(rect.area())) 

    # Example 2: Circle with radius 3
    circle = Circle(3)
    print("{:.2f}".format(circle.area()))
