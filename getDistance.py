from  logDistPathLoss import LogDistPathLoss

import math

class GetDistance:
    def __init__(self,rssi_real):
        self.distance = math.pow(10,((-34.52279052921755 - rssi_real)/33))
        initialised_logDistPathLoss = LogDistPathLoss()
        self.best_answer = [100,0]
        min =1 
        max = 2*round(self.distance)   
        for v1 in range(min,max+1):
            loss = initialised_logDistPathLoss.calc_loss(v1)
            distance = math.pow(10,((-34.52279052921755-loss - rssi_real)/33))
            answer = abs(v1-distance)
            if answer <= self.best_answer[0]:
                self.best_answer[0] = answer
                self.best_answer[1] = v1
        
    def return_value(self):
        return self.best_answer[1]           
