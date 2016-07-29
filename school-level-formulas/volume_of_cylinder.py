from math import pi 

radius = int(raw_input("Enter the radius : "))

height = int(raw_input("Enter the height : "))

def volume_of_cylinder(radius, height):
	volume = pi * (radius **2) * height
	return "Volume of cylinder is %s" % (volume)

print volume_of_cylinder(radius, height)
