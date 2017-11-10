'''import math

radius = float(input("Radius:"))


def sphereArea(radius):
	return math.pi*4*(radius**2)


def sphereVolume(radius):
	return (4*math.pi*(radius**3))/3

print("Surface Area: ", sphereArea(radius), "\nVolume: ", sphereVolume(radius))'''

def Three(n):
	print(n)
	if n % 10 == 3:
		return True
	elif n<9:
		return False
	else:
		return Three(n // 10)

print(Three(int(input("Enter a number:"))))

def isEven(n):
	if n-1==0:
		return False
	else:
		return isOdd(n-1)

def isOdd(n):
	if n-1==0:
		return True
	else:
		return isEven(n-1)

print(isEven(43))

def yes(n):
	if n==0:
		return 0
	print("yes")
	no(n)

def no(n):
	print("no")
	yes(n-1)

yes(3)

def PrintSquares(n):
	if n==1:
		print('1\t1')
		return 0
	else:
		print(n,"\t",n**2)
		PrintSquares(n-1)

PrintSquares(5)

def Sum(n):
	if n==1:
		return 1
	return(n+Sum(n-1))

print(Sum(1))
print(Sum(3))
print(Sum(5))

def F(n):
	if n==0:
		return 1
	if n==1:
		return 1
	return F(n-1)+F(n-2)


print("\n\n")
for i in range(1,10):
	print(F(i))


remPunct = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','\\','|',']','}','{','}','[',"'",'"',';',':','/','?','>','<','.',',']
IsPalindrome(string):
	while list[0] in remPunct:
		del list[0]
	while list[-1] in remPunct:
		del list[-1]



print(IsPalindrome(input("Enter String: ")))



