base = int(raw_input("Enter the base :"))

height = int(raw_input("Enter the height :"))

def area_of_triangle(base, height):
	area = 0.5 * (base * height)
	return "Area of triangle is :%s" % area

print area_of_triangle(base, height)
