# Calculator program that can perform addition, subtraction, multiplication, and division
# and can calculate area and perimeter of different shapes, as well as algebraic expressions
import math
import numpy
import sympy as sp

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def divide(x,y, decimal):
    if y or x == 0:
        return "Error: Division by zero is not allowed"
    result = x / y
    return round(result, decimal)
def multiply(x, y):
    return x * y
def area(shape):
    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        return math.pi * (radius ** 2)
    elif shape == "rectangle":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        return width * height
    elif shape == "triangle":
        type = input("What type of triangle is it? (right, isosceles, equilateral): ")
        if type.lower() == "right":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            return 0.5 * base * height
        elif type.lower == "isosceles":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            return height * base / 2
        elif type.lower() == "equilateral":
            side = float(input("Enter the length of the side of the triangle: "))
            return (side ** 2) * math.sqrt(3) / 4
        else:
            return "Error: Invalid triangle"
    elif shape == "square":
        side = float(input("Enter the length of the side of the square: "))
        return side ** 2


def show_menu():
    choices = [
        {"choice": "1", "function": "add"},
        {"choice": "2", "function": "sub"},
        {"choice": "3", "function": "multiply"},
        {"choice": "4", "function": "divide"},
        {"choice": "5", "function": "area"},

    ]
    choice = input("Enter your choice: ")
    for choice in choices:
        if choice["choice"] == choice:
            if choice["function"] == "area":
                shape = input("Enter the shape: ")
                area(shape)
            
    