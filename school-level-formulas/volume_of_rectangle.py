length = int(raw_input("Enter length of rectangle : "))

width = int(raw_input("Enter width of rectangle : "))

height = int(raw_input("Enter height of rectangle : "))

def volume_of_rectangle(length, width, height):
	volume = length * width * height
	return "Volume of rectangle is : %s" %(volume)


print volume_of_rectangle(length, width, height)
