# Exercise 1:
# Develop a program called Lab5Exc1 that uses methods to complete the following operations:
# • Read a radius decimal value from STDIN
# • Calculate the perimeter of a circle using the radius
# • Calculate the area of a disk using the radius
# • Calculate the volume of a sphere using the radius
# • Show calculated values on separate lines (at 3-decimal points format)

import math


def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return round(perimeter, 3)


def calculate_area(radius):
    area = math.pi * radius**2
    return round(area, 3)


def calculate_volume(radius):
    volume = (4 / 3) * math.pi * radius**3
    return round(volume, 3)


def Lab5Exc1():
    radius = float(input("Enter the radius: "))

    perimeter = calculate_perimeter(radius)
    area = calculate_area(radius)
    volume = calculate_volume(radius)

    print("Perimeter of the circle:", perimeter)
    print("Area of the disk:", area)
    print("Volume of the sphere:", volume)


Lab5Exc1()
