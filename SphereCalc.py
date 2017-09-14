import math

radius = float(input("Radius:"))


def sphereArea(radius):
	return math.pi*4*(radius**2)


def sphereVolume(radius):
	return (4*math.pi*(radius**3))/3

print("Surface Area: ", sphereArea(radius), "\nVolume: ", sphereVolume(radius))