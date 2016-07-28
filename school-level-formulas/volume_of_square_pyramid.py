base_length = float(raw_input("Enter the base length value : "))

height = float(raw_input("Enter the height value : "))

def volume_of_square_pyramid(base_length, height):
	volume = (1.0/3) * (base_length**2) * height 
	return "Volume of square pyramid is %s" % (volume)

print volume_of_square_pyramid(base_length, height)


