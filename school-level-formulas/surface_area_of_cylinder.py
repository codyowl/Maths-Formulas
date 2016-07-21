from math import pi

radius = int(raw_input("Enter the radius :"))

height = int(raw_input("Enter the height :"))

def surface_area_of_cylinder(radius, height):
	area = 2 * pi * radius * height
	return "Surface area of cylinder is %s" % (area)


print surface_area_of_cylinder(radius, height)
