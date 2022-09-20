import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import pickle


class Map:
    def __init__(self,newMap = True,pos = [0,0,0]):
        if newMap:
            self.map = np.full((930,1530),0.5)
            self.roomDetails()
            print("Creating map ...")
            self.addRooms()
            self.save_map()

        else:
            try:
                infile = open("house_map.txt","rb")
            except:
                return None    
            try:
                self.map = pickle.load(infile)
            except:
                print("Couldn't update map")    
            finally:
                infile.close()
        self.mark_beacon(pos)        
        print("Launching map ...")
        self.fig= plt.figure()
        try:
            self.im = plt.imshow(self.map, interpolation='none',cmap='gray', vmin=0, vmax=1)
        except AttributeError:
            pass    
        pass    

    def roomDetails(self):
        self.green_room = [590,910,1100,1520,True,510,590,1100,1150]
        self.pink_room = [10,330,1100,1520,True,330,410,1100,1150]
        self.blue_room = [10,330,710,1010,True,330,410,710,825]
        self.gallery = [400,510,160,1150,False]
        self.drawing_room = [510,910,160,690,False]
        self.hall_way = [480,710,10,160,False]
        self.kitchen = [210,410,10,160,False]
        self.dinning_room = [80,410,160,680,False]
        self.house = [self.green_room,self.pink_room,self.blue_room,self.gallery,self.drawing_room,self.hall_way,self.kitchen,self.dinning_room]

    def mark_beacon(self,pos):
        beacon = [[890,630],[890,180],[530,180]]
        for v1 in beacon:
            for v2 in range(v1[0]-20,v1[0]+21):
                for v3 in range(v1[1]-20,v1[1]+21):
                    self.map[v2][v3] = 0.35
        mark_pos = [100*pos[0],100*pos[1]]
        for v1 in range(870-int(mark_pos[0]),910-int(mark_pos[0])):
            for v2 in range(160+int(mark_pos[1]),200+int(mark_pos[1])):
                self.map[v1][v2] = 0.05

    def addRooms(self):
        for v1 in self.house:
            for v2 in range(v1[0],v1[1]):
                for v3 in range(v1[2],v1[3]):
                    self.map[v2][v3] = 0.8
            if v1[4] == True:
                for v2 in range(v1[5],v1[6]):
                    for v3 in range(v1[7],v1[8]):
                        self.map[v2][v3] = 0.8

    def save_map(self):
        outfile= open("house_map.txt","wb")
        pickle.dump(self.map,outfile)
        outfile.close()

    def view_map(self,i):
        try:
            self.im.set_data(self.map)                                                     
        except:
            pass                
        return self.im    

    def launcher(self):
        anim = animation.FuncAnimation(self.fig, self.view_map,interval=10)
        plt.show()




