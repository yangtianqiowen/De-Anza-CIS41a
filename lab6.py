'''
CIS 41A Lab6
Tianqi Yang
'''
import io

def analyze(filename):
    a = 0 #Number of 'a' counter
    e = 0 #Number of 'e' counter
    i = 0 #Number of 'i' counter
    o = 0 #Number of 'o' counter
    u = 0 #Number of 'u' counter
    total = 0 #Number of 'total' counter
    #Opening the file with encoding = latin-1
    f = io.open(filename, encoding = "latin-1")
    v = ['a','e','i','o','u']#List containing vowels.
    #Reading each line of the file
    for line in f.readlines():
    #Each character of the line
        for ch in line:#Comparing with vowels and incrementing the count.
            #if ch.lower() == 'a'.lower():
                #a += 1
            #if ch.lower() == 'e'.lower():
                #e += 1
            #if ch.lower() == 'i'.lower():
                #i += 1
            #if ch.lower() == 'o'.lower():
                #o += 1
            #if ch.lower() == 'u'.lower():
                #u += 1
            #if ch.isalpha():
                #total += 1
            if ch in "AEIOU":
                vowelsDict[c]+=1
                # if empty dictionary 
                vowelsDict[c] = vowelDict.get(c,0) + 1 

    

    print ("A : {}\nE : {}\nI : {}\nO : {}\nU : {}".format(a, e, i, o, u))
    vowels = a + e + i + o + u

    #print "Total = ",total
    ratio = (vowels / total) * 100
    print ("Total vowels / total letters:", "%.2f" %ratio + "%") #Ratio

def main():
#List containing filenames.
    filenames = ['english.txt', 'french.txt', 'german.txt', 'italian.txt', 'spanish.txt']
    for i in filenames:
        print(i[0].upper()+i[1:-4])
        analyze(i)


main()  