from math import pow

s = int(raw_input("Enter the side value :"))

def surface_area_of_cube(s):
	area = 6 * (pow(s, 2))
	return "Surface area of cube is %s" % (area)


print surface_area_of_cube(s)
