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
'''
punctmylist = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','\\','|',']','}','{','}','[',"'",'"',';',':','/','?','>','<', '.',',']

def IsPalindrome(string):
    mylist = []
    # moves items from string to mylist, removing all punctuation
    for i in string:
        if i not in punctmylist:
            mylist.append(i)
    # lowercases all letters
    for i in range(0,len(mylist)):
        mylist[i] = mylist[i].lower()
    # base cases
    if len(mylist) == 0 or len(mylist)==1:
        return 'isPalindrome'
    # recursion
    # if palindrome so far, remove correct characters and repopulate string, passing it back to IsPalindrome
    elif mylist[0]==mylist[-1]:
        string = ''
        del mylist[0]
        del mylist[-1]
        for i in mylist:
            string += i
        return IsPalindrome(string)
    else:
        return 'isNotPalindrome'


print(IsPalindrome(input("Enter String: ")))




'''

global Solutions
Solutions = 0
def placeQueen(mylist=[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]],queensLeft=8):
#whole else statement makes mylist of positions a queen can go in
    if queensLeft >0:
        mylistPossiblex = []
        mylistPossibley = []
        for x in range(0,8):
            for y in range(0,8):
                canPlace = True
                #checks if there are any other queens in the x column for the space
                if 1 in mylist[x]:
                    canPlace = False
                # checks if there are any queens in the y column for the space
                for x2 in range(0,8):
                    if mylist[x2][y]==1:
                        canPlace = False
                # if canPlace == True here, there are no queens directly down or up or left or right
                #check for diagonal queens
                x3=x
                y3=y
                while x3<=7 and y3<=7:
                    if mylist[x3][y3] ==1:
                        canPlace = False
                        break
                    x3,y3 = x3+1,y3+1
                x3 = x
                y3 = y
                while x3>=0 and y3>=0:
                    if mylist[x3][y3] ==1:
                        canPlace = False
                        break
                    x3,y3 = x3-1,y3-1
                x3=x
                y3=y

                while x3<=7 and y3>=0:
                    if mylist[x3][y3] ==1:
                        canPlace = False
                        break
                    x3,y3 = x3+1,y3-1
                x3 = x
                y3 = y

                while x3>=0 and y3<=7:
                    if mylist[x3][y3] ==1:
                        canPlace = False
                        break
                    x3,y3 = x3-1,y3+1
                if canPlace == True:
                    mylistPossiblex.append(x)
                    mylistPossibley.append(y)
        # for each possible place you can put this queen,
        for i in range(0,len(mylistPossiblex)):
            #make the possible move
            mylist[mylistPossiblex[i]][mylistPossibley[i]] = 1
            #run the function again on this tempmylist with one move made
            placeQueen(mylist,queensLeft = queensLeft-1)
            works = True
            for x in range(0,8):
                if 1 not in mylist[x]:
                    works = False
                    break
                if mylist[x].count(1) >1:
                    works = False
                    break
            if works == False:
                mylist[mylistPossiblex[i]][mylistPossibley[i]] = 0
            if works == True:
                for x in range(0,8):
                    print(mylist[x])
                print()
                global Solutions
                Solutions += 1


print(placeQueen())
print(Solutions)

'''