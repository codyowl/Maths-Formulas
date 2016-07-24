first_side = int(raw_input("Enter first side value : "))

second_side = int(raw_input("Enter second side value : "))

third_side = int(raw_input("Enter third side value : "))


def perimeter_of_triangle(s1, s2, s3):
	perimeter = s1 + s2 + s3
	return "Perimeter is %s" % (perimeter)


print perimeter_of_triangle(first_side, second_side, third_side)
