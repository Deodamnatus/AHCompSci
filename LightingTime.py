# find distance to a lightning strike based on times


# get input and output answers
def main():
    timeBetween = float(input("Enter the time between flash and sound of thunder(sec)\n:"))
    print("\nThere was", calculateDistance(timeBetween), "miles between you and where the lightning struck")

def calculateDistance(time):
    return (time*1100)/5280

main()
