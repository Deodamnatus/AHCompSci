'''import math

radius = float(input("Radius:"))


def sphereArea(radius):
	return math.pi*4*(radius**2)


def sphereVolume(radius):
	return (4*math.pi*(radius**3))/3

print("Surface Area: ", sphereArea(radius), "\nVolume: ", sphereVolume(radius))'''

'''
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

'''

global Solutions
Solutions = 0
def placeQueen(list=[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]],queensLeft=8):
#whole else statement makes list of positions a queen can go in
if queensLeft >0:
    listPossiblex = []
    listPossibley = []
    for x in range(0,8):
        for y in range(0,8):
        canPlace = True
        #checks if there are any other queens in the x column for the space
        if 1 in list[x]:
            canPlace = False
        # checks if there are any queens in the y column for the space
        for x2 in range(0,8):
            if list[x2][y]==1:
                canPlace = False
        # if canPlace == True here, there are no queens directly down or up or left or right
        #check for diagonal queens
        x3=x
        y3=y
        while x3<=7 and y3<=7:
            if list[x3][y3] ==1:
                canPlace = False
                break
            x3,y3 = x3+1,y3+1
        x3 = x
        y3 = y
        while x3>=0 and y3>=0:
            if list[x3][y3] ==1:
                canPlace = False
                break
            x3,y3 = x3-1,y3-1
        x3=x
        y3=y

        while x3<=7 and y3>=0:
            if list[x3][y3] ==1:
                canPlace = False
                break
            x3,y3 = x3+1,y3-1
        x3 = x
        y3 = y

        while x3>=0 and y3<=7:
            if list[x3][y3] ==1:
                canPlace = False
                break
            x3,y3 = x3-1,y3+1
        if canPlace == True:
            listPossiblex.append(x)
            listPossibley.append(y)
    # for each possible place you can put this queen,
    for i in range(0,len(listPossiblex)):
        #make the possible move
        list[listPossiblex[i]][listPossibley[i]] = 1
        #run the function again on this templist with one move made
        placeQueen(list,queensLeft = queensLeft-1)
        works = True
        for x in range(0,8):
            if 1 not in list[x]:
                works = False
                break
            if list[x].count(1) >1:
                works = False
                break
        if works == False:
            list[listPossiblex[i]][listPossibley[i]] = 0
        if works == True:
            for x in range(0,8):
                print(list[x])
            print()
            global Solutions
            Solutions += 1


print(placeQueen())
print(Solutions)

