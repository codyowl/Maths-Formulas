from math import pow
from math import pi


radius = int(raw_input("Enter the radius : "))

def surface_area(radius, PI):
	area = 4 * PI * pow(radius , 2)
	return "Area of sphere is %s" % (area)

print surface_area(radius, pi)
