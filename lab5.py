#CIS 41A
#lab 5
#Yuxi Yu
#Tianqi Yang

def readChart ():
    '''read data from input file
       store data into seating chart
       call printChart()
    '''
    rowCount = 0
    colCount = 0
    table = []
    row=[]    
    while True:
        try:
            fileName = input("Enter file name or hit Enter for default lab5input2.txt: ")
            if fileName =="":
                fileName ="lab5input2.txt"
    
            f = open(fileName, "r")
            r = list(f.read().split(" ")) #take the space between each number
            count = 0
            while count < len(r):
                if not r[count]:
                    del r[count]
                    continue
                if "\n" in r[count]:
                    r[count] = r[count].split("\n")[1]
                    table.append(row)
                    row=[]
                else:
                    r[count] = r[count].rstrip()
                    row.append(r[count])
                    count+=1
            rowCount,colCount = printChart(table)
            break
        except IOError:
            print("Can't open", fileName)
        
        except ValueError as error:
            print ("Error:", str(error))
    return table,rowCount,colCount

    
    
    
def buySeat(table,row,col):
    '''ask user the seats by row and table
       if seat available 
       -add up the price 
       -mark the seat with an 'x'
       -save the seat(row, col)
       print the total price
       call printChart()
    '''
    print("Available seats are shown with price")
    broughtSeat = []
    repeat = False
    while True:
        
            raw_input = input("Enter row,col for seat " + str(len(broughtSeat) + 1) + " or enter 0 to end: ")
            if raw_input == "0":
                break
            if "," not in raw_input:
                print("Invalid input")
                continue
            user_input = (raw_input.split(',')[0],raw_input.split(',')[1])
            if (not user_input[0].lstrip('-').isdigit()) or (not user_input[1].lstrip('-').isdigit()):
                print("Row and column must be numbers")
                continue
            elif int(user_input[0])>row or int(user_input[1])>col or int(user_input[0])<1 or int(user_input[1])<1:
                print("Invalid row or column")
                continue
            if "-" in table[int(user_input[0])-1][int(user_input[1])-1]:
                repeat = True
            for i in range(len(broughtSeat)):
                if (user_input == broughtSeat[i]):
                    repeat = True
            if repeat:
                repeat = False
                print("Sorry, that seat is not available.")
                continue
            broughtSeat.append(user_input)
            
    ticketCost = 0
    totalSeat = ""
    for i in range (len(broughtSeat)):
        ticketCost += int(table[int(broughtSeat[i][0])-1][int(broughtSeat[i][1])-1])
        totalSeat += "(" + broughtSeat[i][0] + ", " + broughtSeat[i][1] + ") " 
        table[int(broughtSeat[i][0])-1][int(broughtSeat[i][1])-1] = "  X"
    print()
    print("Your total: $"+str(ticketCost))
    print("Your "+str(len(broughtSeat)) + " seat(s) at " + totalSeat + "are marked with 'X'")
    
    printChart(table)

    
    
    
    
    
    
    
def saveChart(table,row,col):
    '''save the seat by prompting the user for an output file
       or hit Enter to save to the default lab5input2.txt
       when saving the seating chart, 'x' is save as'--'
    '''
    foutName = input("Enter file name or hit Enter for default lab5input2.txt: ")
    if foutName == "":
        foutName = "lab5input2.txt"

    for i in range (row):
        for j in range (col):
            if table[i][j] == "  X":
                table[i][j] = " --"

    with open(foutName, "w") as outfile:
        for i in range(row):
            for j in range(col):
                val = table[i][j]
                outfile.write(val + " ")
            outfile.write("\n")

    print(foutName, "updated")
    
    
    
    
def printChart(t):
    '''print the seating chart
    '''
    row = 0
    col = 0
    dataCount = 0
    print("                 Price chart")
    print("                    Column")
    for i in range(len(t[0])):
        if i+1 == 1:
            print("      " ,i+1, end='    '),
        else :
            print(i+1,end = '    ')
    print()
    dash = '=====' * len(t[0])
    print('Row ',dash)
    for r in range(len(t)) :
        print(' %d |' % (r+1), end = '')
        row +=1                     # walks each row
        for c in range(len(t[0])) : 
            if 'X' not in t[r][c] and '--' not in t[r][c]:
                string = '$'+t[r][c]

                
            else:
                string = t[r][c]
            print("%5s" % string ,sep = '', end='')
            dataCount += 1                # walks each col of a row
   
        print ()     # to print a new line
    print()
    col = dataCount//row
    return row,col
    

def main():
    '''main funciton that call all other functions
    '''
    table,row,col = readChart()
    buySeat(table,row,col)
    saveChart(table,row,col)
    
    
    
    
main()

