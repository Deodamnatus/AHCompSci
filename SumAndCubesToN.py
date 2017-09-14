n = int(input("N: "))

def sumN(N):
    sumOfN = 0
    for i in range(0,N+1):
        sumOfN += i
    return sumOfN

def sumNCubes(N):
    sumOfNNN = 0
    for i in range(0, N + 1):
        sumOfNNN += i**3
    return sumOfNNN

print("Sum: ", sumN(n), "\nSum of cubes: ", sumNCubes(n))