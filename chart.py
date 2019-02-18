'''
lab7 
Yuxi Yu
Tianqi Yang
'''

from seat import Seat, Premium, Choice, Regular

class Chart:

    def __init__(self, chart=[]):
        '''constructor
           read the file in the the list
           store the row and col
           call the seat constructor and pass the price to seat
        ''' 
        self._rowCount = 0
        self._colCount = 0
        self._chart = []
        while True:
            try:
                fileName = input("Enter file name or hit Enter for default lab7input2.txt: ")
                if fileName =="":
                    fileName ="lab7input2.txt"
        
                f = open(fileName, "r")
                prices = f.readline().split(" ")
                premium = int(prices[0])
                choice = int(prices[1])
                regular = int(prices[2].strip('\n'))
                
                while True: 
                    currentLine = f.readline()
                    if currentLine == "":
                        break
                    rowOfPrice = list(int(s) for s in currentLine.split() if s.isdigit())
                    row = []
                    for elem in rowOfPrice:
                        if elem == premium:
                            currentSeat = Premium(premium)
                        elif elem == choice:
                            currentSeat = Choice(choice)
                        else:
                            currentSeat = Regular(regular)
                        row.append(currentSeat)
                    self._chart.append(row)
                f.close()
                break
            except IOError:
                print("Can't open", fileName)
                
            except ValueError as error:
                print ("Error:", str(error))
                
        self._rowCount,self._colCount = self.printChart(self._chart)
                
                
    def printChart(self, chart):
        ''' print the price chart and mark the taken seat with X'''
        row = 0
        col = 0
        dataCount = 0
        print("                 Price chart")
        print("                    Column")
        for i in range(len(self._chart[0])):
            if i+1 == 1:
                print("      " ,i+1, end='    '),
            else :
                print(i+1,end = '    ')
        print()
        dash = '=====' * len(self._chart[0])
        print('Row ',dash)
        for r in range(len(self._chart)) :
            print(' %d |' % (r+1), end = '')
            row +=1                     # walks each row
            for c in range(len(self._chart[0])) : 
                if self._chart[r][c].isTaken():
                    string = " X"
                else:
                    string = "$" + str(self._chart[r][c].getPrice())
                print("%5s" % string ,sep = '', end='')
                dataCount += 1                # walks each col of a row
       
            print ()     # to print a new line
        print()
        col = dataCount//row
        return row,col     
        
    
            
    def buySeat(self):
        '''check if the seat is available 
            print the taken seat to user
            calculate the total price
            call the printChart funciton'''
        
        print("Available seats are shown with price")
        repeat = False
        ticketCost = 0
        totalSeat = ""
        broughtSeat = []
        while True:
                
                raw_input = input("Enter row,col for seat " + str(len(broughtSeat) + 1) + " or enter 0 to end: ")
                if raw_input == "0":
                    break
                if "," not in raw_input:
                    print("Invalid input")
                    continue
                user_input = (raw_input.split(',')[0],raw_input.split(',')[1])
                if (not user_input[0].lstrip('-').isdigit()) or (not user_input[1].lstrip('-').isdigit()):
                    print("Invalid row or column")
                    continue
                elif int(user_input[0])>self._rowCount or int(user_input[1])>self._colCount or int(user_input[0])<1 or int(user_input[1])<1:
                    print("Invalid row or column")
                    continue
                for i in range(len(broughtSeat)):
                    if (user_input == broughtSeat[i]):
                        self._chart[int(user_input[0])-1][int(user_input[1])-1].setTaken()
                if self._chart[int(user_input[0])-1][int(user_input[1])-1].isTaken() == True:

                    print("Sorry, that seat is not available.")
                    continue
                broughtSeat.append(user_input)
                ticketCost += int(self._chart[int(user_input[0])-1][int(user_input[1])-1].getPrice())
                totalSeat += "(" + user_input[0] + ", " + user_input[1] + ") " 
                self._chart[int(user_input[0])-1][int(user_input[1])-1].setTaken()          
        print()
        print("Your total: $"+str(ticketCost))
        print("Your "+str(len(broughtSeat)) + " seat(s) at: ")
        for elem in range (len(broughtSeat)):
            print("Row" , broughtSeat[elem][0], "column", broughtSeat[elem][1],":", self._chart[int(broughtSeat[elem][0])-1][int(broughtSeat[elem][1])-1].getExtra())
        print("Your seats are marked with 'X' below")
        
        self.printChart(self._chart)        
               