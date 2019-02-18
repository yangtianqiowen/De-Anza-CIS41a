'''
Tianqi Yang
Yuxi Yu
Lab 7
11/17
'''
class Seat:
    
    def __init__(self, price = 0, taken = False):
        '''constructor set the instance variable'''
        self._price = price
        self._taken = taken
        
    def getExtra(self):
        raise NotImplementedError
    
    def getPrice(self):
        '''return price'''
        return self._price
    
    def isTaken(self):
        '''return if the seat is taken'''
        return self._taken 
    
    def setTaken(self):
        '''set taken to true if seat is taken, because taken is a private instance variable'''
        self._taken = True
    
class Premium(Seat):
    
    def __init__(self, price):
        '''call the super class constructor'''
        super().__init__(price)
        
    def getExtra(self):
        '''return the extra perk string'''
        return "your swag bag and drink ticket are at will call"
    
class Choice(Seat):
    
    def __init__(self, price):
        '''call the super class constructor'''
        super().__init__(price)
        
    def getExtra(self):
        '''return the extra perk string'''
        return "your drink ticket are at will call     "
    
class Regular(Seat):
    
    def __init__(self, price):
        '''call the super class constructor'''
        super().__init__(price)
        
    def getExtra(self):
        '''return the extra perk string'''
        return "drinks are available for purchase at intermission"