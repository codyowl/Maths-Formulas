from math import pi

radius = int(raw_input("Enter the radius : "))

height = int(raw_input("Enter the height : "))

def volume_of_cone(radius, height):
	volume = (1.0/3) * pi * (radius**2) * height 
	return "Volume of volume is %s" % (volume)

print volume_of_cone(radius, height)
