length = int(raw_input("Enter the length :"))

width = int(raw_input("Enter the width :"))

def area_of_rectangle(length, width):
	area = length * width
	return "Area of rectangle is : %s" % (area) 

print area_of_rectangle(length, width)
