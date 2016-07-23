length = int(raw_input("Enter length value :"))

width = int(raw_input("Enter the width value :"))

def perimeter_of_rectange(length, width):
	perimeter = (2 * length) + (2 * width)
	return "Perimeter of rectangle with length %s and width %s is %s" % (length, width, perimeter)


print perimeter_of_rectange(length, width)


