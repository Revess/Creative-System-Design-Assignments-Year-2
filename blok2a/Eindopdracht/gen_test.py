import time
import random

bpm = 120
tempo = 60 / bpm
timestamps = [0]
rhythm = []
rhythm_obj_lst = [1,2,4,8,16]
timestampKick = []
timestampSnare = []
timestampHat = []
plays = 5
measure = ['7','4']
command = 'generate'
percentages = [100,[50,50],[10,60,30],[10,15,50,25],[7.5,12.5,20,40,20]]

def shuffleLst(lst):                                #Will shuffle a given list
    length = len(lst)
    rnd = round((length*random.random()))           #Generate two random values according to the length of the list
    rnd2 = round((length*random.random()))
    val = lst[0]                                    #Pick the first and the last item of the list
    lst.remove(val)
    lst.reverse()
    val2 = lst[0]
    lst.remove(val2)
    lst.reverse()
    lst.insert(rnd, val)                            #Insert both items on a random spot in the list
    lst.insert(rnd2, val2)
    return lst

def lowGen(count,val,lst):
    global percentages,tempo
    count = count*(tempo/(val/val))
    pos = 0
    offset = 100*random.random()
    bitoff = False
    while count > pos:
        rnd = 100*random.random()
        if val == 1:
            lst.append(1)
        elif val == 2:
            if rnd <= percentages[1][0]:
                lst.append(1)
            elif rnd > percentages[1][1]:
                lst.append(2)
        elif val == 4:
            if rnd <= percentages[2][0]:
                lst.append(1)
            elif rnd > percentages[2][0] and rnd <= percentages[2][0]+percentages[2][1]:
                lst.append(2)
            elif rnd > percentages[2][0]+percentages[2][1]:
                lst.append(4)
        elif val == 8:
            if rnd <= percentages[3][0]:
                lst.append(1)
            elif rnd > percentages[3][0] and rnd <= percentages[3][0]+percentages[3][1]:
                lst.append(2)
            elif rnd > percentages[3][0]+percentages[3][1] and rnd <= percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(4)
            elif rnd > percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(8)
        elif val == 16:
            if rnd <= percentages[4][0]:
                lst.append(1)
            elif rnd > percentages[4][0] and rnd <= percentages[4][0]+percentages[4][1]:
                lst.append(2)
            elif rnd > percentages[4][0]+percentages[4][1] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]:
                lst.append(4)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(8)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(16)
        lst.reverse()
        lst[0]/=val 
        lst[0]=tempo/lst[0]
        pos += lst[0]
        lst.reverse()
    if pos > count:
        dif = 0
        if offset <= 25:
            offset = (tempo/(val/val))/2
            dif = (pos - count)+offset
        else:
            dif = (pos - count)
        lst.reverse()
        lst[0]-=dif
        if lst[0] < 0:
            lst[1]+=lst[0]
            lst.remove(lst[0])
        lst.reverse()
    if not bitoff:
        offset = 0
    lst.append(offset)
    return lst

def midGen(count,val,lst):
    global percentages,tempo
    count = count*(tempo/(val/val))
    pos = 0
    offset = 100*random.random()
    bitoff = False
    while count > pos:
        rnd = 100*random.random()
        if val == 1:
            if rnd <= percentages[1][0]:
                lst.append(1)
            elif rnd > percentages[1][1]:
                lst.append(2)
        elif val == 2:
            if rnd <= percentages[2][0]:
                lst.append(1)
            elif rnd > percentages[2][0] and rnd <= percentages[2][0]+percentages[2][1]:
                lst.append(2)
            elif rnd > percentages[2][0]+percentages[2][1]:
                lst.append(4)
        elif val == 4:
            if rnd <= percentages[3][0]:
                lst.append(1)
            elif rnd > percentages[3][0] and rnd <= percentages[3][0]+percentages[3][1]:
                lst.append(2)
            elif rnd > percentages[3][0]+percentages[3][1] and rnd <= percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(4)
            elif rnd > percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(8)
        elif val == 8:
            if rnd <= percentages[4][0]:
                lst.append(1)
            elif rnd > percentages[4][0] and rnd <= percentages[4][0]+percentages[4][1]:
                lst.append(2)
            elif rnd > percentages[4][0]+percentages[4][1] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]:
                lst.append(4)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(8)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(16)        
        elif val == 16:
            if rnd <= percentages[4][0]:
                lst.append(1)
            elif rnd > percentages[4][0] and rnd <= percentages[4][0]+percentages[4][1]:
                lst.append(2)
            elif rnd > percentages[4][0]+percentages[4][1] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]:
                lst.append(4)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(8)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(16)
        lst.reverse()
        lst[0]/=val 
        lst[0]=tempo/lst[0]
        pos += lst[0]
        lst.reverse()
    if pos > count:
        dif = 0
        if offset <= 80:
            offset = tempo/(val/val)
            dif = (pos - count)+offset
            bitoff = True
        else:
            dif = (pos - count)
        lst.reverse()
        lst[0]-=dif
        if lst[0] < 0:
            lst[1]+=lst[0]
            lst.remove(lst[0])
        lst.reverse()
    if not bitoff:
        offset = 0
    lst.append(offset)
    return lst

def highGen(count,val,lst):
    global percentages,tempo
    count = count*(tempo/(val/val))
    pos = 0
    offset = 100*random.random()
    bitoff = False
    while count > pos:
        rnd = 100*random.random()
        if rnd <= percentages[4][0]:
            lst.append(1)
        elif rnd > percentages[4][0] and rnd <= percentages[4][0]+percentages[4][1]:
            lst.append(2)
        elif rnd > percentages[4][0]+percentages[4][1] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]:
            lst.append(4)
        elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
            lst.append(8)
        elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
            lst.append(16)
        lst.reverse()
        lst[0]/=val 
        lst[0]=tempo/lst[0]
        pos += lst[0]
        lst.reverse()
    if pos > count:
        dif = 0
        if offset <= 15:
            offset = (tempo/(val/val))/2
            dif = (pos - count)+offset
        else:
            dif = (pos - count)
        lst.reverse()
        lst[0]-=dif
        if lst[0] < 0:
            lst[1]+=lst[0]
            lst.remove(lst[0])
        lst.reverse()
    if not bitoff:
        offset = 0
    lst.append(offset)
    return lst

def beatGen(count, val):
    global timestampKick, timestampSnare, timestampHat, command
    beatCount = int(count)
    oneBeatVal = int(val)
    #While True: Enable when implementing Threading
    if command == 'generate':
        lowGen(beatCount,oneBeatVal,timestampKick)
        midGen(beatCount,oneBeatVal,timestampSnare)
        highGen(beatCount,oneBeatVal,timestampHat)
    else:
        time.sleep(0.001)

beatGen(measure[0],measure[1])