import time
import random
import threading
from threading import Thread
from random import shuffle

bpm = 120
tempo = 60 / bpm
timestamps = [0]
rhythm = []
rhythm_obj_lst = [1,2,4,8,16]
rhythmKick = []
rhythmSnare = []
rhythmHat = []
timestampKick = []
timestampSnare = []
timestampHat = []
plays = 1
measure = ['4','4']
command = 'generate'
percentages = [100,[50,50],[10,60,30],[10,15,50,25],[7.5,12.5,20,40,20]]

def convertToStamps(lst):                           #Convert a list to timestamps
    stamps = []
    ms_lst = lst.copy()
    offset = ms_lst.pop()
    x = 0 + offset                                  #The old timestamp value is x
    stamps.insert(0,x)                              #Make the starting sample start on timestamp 0
    #while count > 0:                               #If we still didn't get to the end of the requested amount of loops repeat
    for f in ms_lst:                                #For every floatingpoint number in the millisecond list
        x += f                                      #Add the current floatingpoint to the previous one, the new timestamp is created
        stamps.append(x)                            #Add this timestamp to the list
    #    count -= 1                                 #One loop is compleated substract one
    #    shuffle(ms_lst)                            #Mix the old rhythm playlist so we can generate more random lists (See the function for explanation)
    stamps.pop()                                    #Remove the last stamp to so the offset we created at the start (insert a 0) works right
    return stamps


def Gen(count,val,lst,layer):
    global percentages,tempo
    layer*=val
    if layer > 16:
        layer = 16
    count = count*(tempo/(val/val))                 #Transforms the musical terminology to floating point numbers in milliseconds according to the BPM. 
                                                    #7/4 with a bpm of 120 will make it 3.5/4, because one quarter note will be 0.5ms there will fit 7 quarter notes in one measure
    pos = 0                                         #Tracks the position of how long one measure will be
    offset = 100*random.random()                    #Create random value for the offset chance
    bitoff = False                                  #Offset is set to 0 right now
    while count > pos:
        rnd = 100*random.random()
        if layer == 1:                                #If the measure is x/1 the kick can only append a whole note
            lst.append(1)
        elif layer == 2:                              #If the measure is x/2 the kick can only append a whole or half note (50/50)
            if rnd <= percentages[1][0]:
                lst.append(1)
            elif rnd > percentages[1][1]:
                lst.append(2)
        elif layer == 4:                              #If the measure is x/4 the kick can only append a whole, half or quarter note (10/60/30)
            if rnd <= percentages[2][0]:
                lst.append(1)
            elif rnd > percentages[2][0] and rnd <= percentages[2][0]+percentages[2][1]:
                lst.append(2)
            elif rnd > percentages[2][0]+percentages[2][1]:
                lst.append(4)
        elif layer == 8:                              #If the measure is x/8 the kick can only append a whole, half, quarter or eight note (10/15/50/25)
            if rnd <= percentages[3][0]:
                lst.append(1)
            elif rnd > percentages[3][0] and rnd <= percentages[3][0]+percentages[3][1]:
                lst.append(2)
            elif rnd > percentages[3][0]+percentages[3][1] and rnd <= percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(4)
            elif rnd > percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(8)
        elif layer == 16:                             #If the measure is x/16 the kick can only append a whole, half, quarter, eight or sixteenth note (7.5/12.5/20/40/20)
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
        lst.reverse()                               #Get the last element
        lst[0]/=4                                 #Transform the note to floatingpoint in ratio
        lst[0]=tempo/lst[0]                         #Transform to milliseconds
        pos += lst[0]                               #The measure will fill up according to the length of the generated note
        lst.reverse()                               #Put the value back at the end
    if pos > count:                                 #If list is overcounted check by how much and remove the difference
        dif = 0
        if offset <= 25:                            #25% chance there will be an offset for the kick
            offset = (tempo/(val/val))/2
            dif = (pos - count)+offset
        else:
            dif = (pos - count)                     #Calculate the difference of the overcount
        lst.reverse()                               #Get the last element
        lst[0]-=dif                                 #Substract the difference of the overcount so the note will fit in one measure
        if lst[0] < 0:                              #If negative number (due to substraction) it means the substraction hasn't been completed.
            lst[1]+=lst[0]                          #Now the list will add its negative member to break even.
            lst.remove(lst[0])                      #And remove the negative number
        lst.reverse()                               #Put te value back at the end
    if not bitoff:                                  #Makes sure the offset will be 0 if the chances weren't correct
        offset = 0
    count = plays
    shuffledlst = lst.copy()
    while count > 1:
        shuffle(shuffledlst)
        lst = lst+shuffledlst
        count-=1
    lst.append(offset)                              #Add the offset at the end for the timestamp calculations
    return lst

def beatGen(count, val):                            #Generate a rhythm ready to play args is the measure
    global timestampKick, timestampSnare, timestampHat, rhythmKick, rhythmSnare, rhythmHat, command
    beatCount = int(count)
    oneBeatVal = int(val)
    count = plays
    #While True: Enable when implementing Threading
    if command == 'generate':
        rhythmKick = []                             #Empty the lists
        rhythmSnare = []
        rhythmHat = []
        timestampKick = []
        timestampSnare = []
        timestampHat = []
        rhythmKick = Gen(beatCount,oneBeatVal,rhythmKick,1)
        rhythmSnare = Gen(beatCount,oneBeatVal,rhythmSnare,2)
        rhythmHat = Gen(beatCount,oneBeatVal,rhythmHat,4)
        timestampKick = convertToStamps(rhythmKick)
        timestampSnare = convertToStamps(rhythmSnare)
        timestampHat = convertToStamps(rhythmHat)
    else:
        time.sleep(0.001)
    print(timestampKick)
    print(timestampSnare)
    print(timestampHat)

beatGen(measure[0],measure[1])
