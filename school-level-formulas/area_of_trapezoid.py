
base_1 = int(raw_input("Enter base1 value :"))

base_2 = int(raw_input("Enter base2 value :"))

height = int(raw_input("Enter height value :"))

def area_of_trapezoid(base_1, base_2, height):
	area = 0.5* (base_1 + base_2) * height
	return "Area of trapezoid is: %s" % (area)


print area_of_trapezoid(base_1, base_2, height)
