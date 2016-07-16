from math import pow

PI = 3.14

radius = int(raw_input("Enter the value of radius : "))

def area_of_circle(radius, pi):
	area = pi * pow(radius, 2)
	print "Area of circle is %s" % area

area_of_circle(radius, PI)
	

