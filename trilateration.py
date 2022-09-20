import math

class Trilateration:
    def __init__(self):
        self.co_ord1 = [0,0,0]
        self.co_ord2 = [4.6,0,0]
        self.co_ord3 = [0,3.2,0]
        self.position = [0,0,0]
        

    def return_position(self,r1,r2,r3):
        self.position[0]= (math.pow(r1,2)-math.pow(r2,2)+math.pow(self.co_ord2[0],2))/(2*self.co_ord2[0])
        self.position[1]= (math.pow(r1,2)-math.pow(r3,2)+math.pow(self.co_ord3[1],2))/(2*self.co_ord3[1])
        #self.position[2]= -math.pow(math.pow(r1,2)-math.pow(self.position[0],2)-math.pow(self.position[1],2),0.5)
        return self.position
        
