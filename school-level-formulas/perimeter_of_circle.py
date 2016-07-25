from math import pi

diameter = int(raw_input("Enter the diameter : "))

def perimeter_of_circle(diameter):
	perimeter = pi * diameter
	return "Perimeter of circle is %s" % (perimeter)


print perimeter_of_circle(diameter)


