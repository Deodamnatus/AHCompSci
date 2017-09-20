'''
import math

radius = float(input("Radius:"))


def sphereArea(radius):
	return math.pi*4*(radius**2)


def sphereVolume(radius):
	return (4*math.pi*(radius**3))/3

print("Surface Area: ", sphereArea(radius), "\nVolume: ", sphereVolume(radius))
'''

def squareAdd(a,b,c):
    return min(min(max(a,b),max(b,c)),min(max(a,c),max(b,c)),min(max(a,b),max(a,c)))**2 + max(a,b,c)**2

print(squareAdd(1,2,3)