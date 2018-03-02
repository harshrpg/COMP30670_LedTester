class Lights(object):

    def __init__(self, L):
        """Constructor for the class"""
        self.__L = L
        self.__grid = [[False]*self.__L for i in range(self.__L)]
        self.__onCount = 0
        self.__offCount = L*L

    def runCmd(self, method,l1,l2,l3,l4):
        """Commands to test the leds from the grid"""

        if method == "turn on":
            for i,row in enumerate(self.__grid[l2:l4+1]):
                row[l1:l3+1] = [True]*((l3+1)-l1)
        
        elif method == "turn off":
            for i, row in enumerate(self.__grid[l2:l4+1]):
                row[l1:l3+1] = [False]*((l3+1)-l1)
        
        elif method == "switch":
            for i, row in enumerate(self.__grid[l2:l4+1]):
                row[l1:l3+1] = [not col for col in row[l1:l3+1]]

    def counts(self):
        """Counts the total Leds that are on and off"""
        self.__onCount = (sum([row.count(True) for row in self.__grid]))
        self.__offCount = self.__offCount-self.__onCount
        return('LEDS ON: {}, LEDS OFF {}'.format(self.__onCount, self.__offCount))