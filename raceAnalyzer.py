'''
Tianqi Yang
Lab8 
'''
import re

class RaceAnalyzer:

    def __init__(self):
        fp = open('lab8input.txt')
        
        #read and save the data
        self.count = 0
        self.race_by_name = {}
        self.race_by_type = {}
        #dictionary with key = loc, value = times
        self.race_by_location = {}
        #                       name       state  distance          type               time 
        pattern = re.search('   "([^"]+)".*,\s+(..).*(\d+)\s+Mile\s+(open|Masters)\s+\w+\s+([\d:.]+[DNF])   ', line)
        #pattern = re.compile("\"(.+?)\"(.+)\"(.+?)\"\s+(\d+).+(Open|Masters)\s+(Men|Women)\s+(DNF|\d+:\d+:\d+\.\d+).+")
        i = 0
        for line in fp:
         
            match = pattern.search(line.strip())
            
            if match:
                
                name,name2, location, racing_distance, racer_type,racer_type2,finish_time = match.groups()
               
                name = name.strip()
                name2 = name2.strip()
                location = location.strip()
                racing_distance = int(racing_distance.strip())
                racer_type = racer_type.strip()
                finish_time = finish_time.strip()
                LOC = location.split(',')[1].strip()[:2].upper()
                #filter  some data
                if name2.strip('"') == location:
                    continue
                self.count += 1

                #save in race_by_type
                if racing_distance not in self.race_by_type:

                    self.race_by_type[racing_distance] = {}
                if racer_type not in self.race_by_type[racing_distance]:
                    self.race_by_type[racing_distance][racer_type] = []

                self.race_by_type[racing_distance][racer_type].append(name.title())
                #save in race location
                if LOC not in self.race_by_location:
                    
                    self.race_by_location[LOC] = 0
                
                self.race_by_location[LOC] += 1
                self.race_by_name[name.title()] = [location, racing_distance, racer_type,finish_time]

  
        fp.close()

    def getCount(self):
        
        return self.count


    def searchByName(self):

        while True:

            n = input("Enter a racer full name: ")
            if n.title() not in self.race_by_name:
                
                print('No racer by the name {}'.format(n.title()))
                continue
            else:

                print('Name: {}'.format(n.title()))
                print('Distance: {} miles'.format(self.race_by_name[n.title()][1]))
                print('Time: {}'.format(self.race_by_name[n.title()][3]))
                return


    def searchByType(self):

        for dis in sorted(self.race_by_type.keys()):

            #show open
            print('  Open')
            for i in sorted(self.race_by_type[dis]['Open']):

                print(i)

            print('{} racers in the {} mile Open race'.format(len(self.race_by_type[dis]['Open']), dis))

            print('  Masters')
            for i in sorted(self.race_by_type[dis]['Masters']):

                print(i)

            print('{} racers in the {} mile Masters race'.format(len(self.race_by_type[dis]['Masters']), dis))
            print()
            
    def searchByLocation(self):

        data = sorted(self.race_by_location.items(), key = lambda x:(x[1], x[0]))
        count_dict = {}
        #change the key value
        for d in data:
            count_dict[d[1]] = []

        for d in data:
            count_dict[d[1]].append(d[0])
        #sorte the dict
        for k,v in sorted(count_dict.items(),reverse = True):
            for v1 in sorted(v):
        
                print('{}: {}'.format(v1,k))
    
