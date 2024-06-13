"""
Daire alanı --> pi*r**2
Daire çevresi --> 2*pi*r
"""

import math

def get_radius():
    return float(input("Yarıçapı giriniz: "))

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

if __name__ == "__main__":
    r = get_radius()
    print("Daire alanı:", circle_area(r))
    print("Daire çevresi:", circle_circumference(r))