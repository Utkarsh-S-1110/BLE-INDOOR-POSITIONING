from kalman_filter import Kalman_Filter
from  logDistPathLoss import LogDistPathLoss
from getDistance import GetDistance
from trilateration import Trilateration
from map import Map

import pickle
import time
import math

cnt = 0
top_ten = [[],[],[]]
rssi_real = [0,0,0]
distance = [0,0,0]

while cnt < 10:
    try:
        infile = open("/usr/local/lib/python3.8/dist-packages/bluepy/rssi_values.txt","rb")
        rssi_list = pickle.load(infile)
        infile.close()
        
        if (rssi_list[0] > -10) or (rssi_list[0] < -99):
            continue
        else:
            top_ten[0].append(rssi_list[0])            
        if (rssi_list[1] > -10) or (rssi_list[1] < -99):
            continue
        else:
            top_ten[1].append(rssi_list[1])
        if (rssi_list[2] > -10) or (rssi_list[2] < -99):
            continue        

        top_ten[2].append(rssi_list[2])
        print(rssi_list)
        cnt+=1
        time.sleep(3)
    except Exception as e:
        print(e)
print("X-----X-----X")        
rssi_real[0] = sum(top_ten[0])/len(top_ten[0])
rssi_real[1] = sum(top_ten[1])/len(top_ten[1])
rssi_real[2] = sum(top_ten[2])/len(top_ten[2])

initialised_klmn_filter0 = Kalman_Filter(rssi_real[0])
initialised_klmn_filter1 = Kalman_Filter(rssi_real[1])
initialised_klmn_filter2 = Kalman_Filter(rssi_real[2])

initialised_logDistPathLoss = LogDistPathLoss()
initialised_trilateration = Trilateration()

cnt = 0

while cnt<5:
    infile = open("/usr/local/lib/python3.8/dist-packages/bluepy/rssi_values.txt","rb")
    rssi_list = pickle.load(infile)
    infile.close()    
    if (rssi_list[0] > -10) or (rssi_list[0] < -99):
        continue
    else:
        rssi_real[0] = initialised_klmn_filter0.find_real(rssi_list[0])
    if (rssi_list[1] > -10) or (rssi_list[1] < -99):
        continue
    else:
        rssi_real[1] = initialised_klmn_filter1.find_real(rssi_list[1])
    if (rssi_list[2] > -10) or (rssi_list[2] < -99):
        continue

    rssi_real[2] = initialised_klmn_filter2.find_real(rssi_list[2])

    getDist = GetDistance(rssi_real[0])
    distance[0] = getDist.return_value()+1

    getDist = GetDistance(rssi_real[1])
    distance[1] = getDist.return_value()+1

    getDist = GetDistance(rssi_real[2])
    distance[2] = getDist.return_value()+1

    print(rssi_real)
    print(distance[0],",",distance[1],",",distance[2])
    print("X-----X-----X")
    time.sleep(2)
    cnt += 1

position = initialised_trilateration.return_position(distance[0],distance[1],distance[2])
initialise_map= Map(newMap = False,pos = position)
initialise_map.launcher()
