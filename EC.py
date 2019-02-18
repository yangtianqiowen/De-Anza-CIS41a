
# List of lists to dictionary extra credit

from seat import Premium, Choice, Regular

# read from file into chart
chart = {}  
with open("lab7input2.txt") as infile:
    (premium, choice, regular) = infile.readline().split()
    row = 0
    for line in infile :   
        col = 0
        for item in line.split() :   
            if item == premium :
                seat = Premium(premium)
            elif item == choice :
                seat = Choice(choice)
            else :
                seat = Regular(regular)
            chart[(row,col)] = seat
            col += 1
        row += 1

for item1 in range(row):    
    for item2 in range(col):
        print("%5s" % chart[(item1,item2)].getPrice(), end="")
    print()         
    
print()   

# buy 3 seats        

for i in range(3) : 
    val = input("Enter row,col: ")
    (rowX, colX) = [int(elem) - 1 for elem in val.split(',')]

    if chart[(rowX,colX)].isTaken() == False :
        chart[(rowX,colX)].setPrice('X')   # set seat to 'X'
        chart[(rowX,colX)].seatIsTaken()
    else:
        print("Sorry, that seat is not available.")
        

# print chart
print()

for item1 in range(row):    
    for item2 in range(col):
        print("%5s" % chart[(item1,item2)].getPrice(), end="")
    print()         
    
print()  