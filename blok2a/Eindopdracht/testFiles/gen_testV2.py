import time
import random
import threading
from threading import Thread
from random import shuffle

bpm = 200
tempo = 60 / bpm
timestamps = [0]
rhythm_obj_lst = [1,2,4,8,16]
rhythmKick = []
rhythmSnare = []
rhythmHat = []
timestampKick = []
timestampSnare = []
timestampHat = []
plays = 1
measure = ['7','8']
command = 'generate'
percentages = [100,[50,50],[10,60,30],[10,15,50,25],[7.5,12.5,20,40,20]]

def convertToStamps(lst):                           #Convert a list to timestamps
    stamps = []
    for f in lst:
        f*=tempo
        stamps.append(f)
    return stamps


def Gen(count,val,lst,layer):
    global percentages
    rhythm = []                                     #List of the exported rhythm
    layer*=val
    val/=4
    if layer > 16:
        layer = 16
    count/=val                                      #Transforms the musical terminology to floating point numbers in milliseconds according to the BPM. 
                                                    #7/4 with a bpm of 120 will make it 3.5/4, because one quarter note will be 0.5ms there will fit 7 quarter notes in one measure
    pos = 0                                         #Tracks the position of how long one measure will be
    offset = 100*random.random()                    #Create random value for the offset chance
    bitoff = False                                  #Offset is set to 0 right now
    while count > pos:
        rnd = 100*random.random()
        if layer == 1:                              #If the measure is x/1 the kick can only append a whole note
            lst.append(4)
        elif layer == 2:                            #If the measure is x/2 the kick can only append a whole or half note (50/50)
            if rnd <= percentages[1][0]:
                lst.append(4)
            elif rnd > percentages[1][1]:
                lst.append(2)
        elif layer == 4:                            #If the measure is x/4 the kick can only append a whole, half or quarter note (10/60/30)
            if rnd <= percentages[2][0]:
                lst.append(4)
            elif rnd > percentages[2][0] and rnd <= percentages[2][0]+percentages[2][1]:
                lst.append(2)
            elif rnd > percentages[2][0]+percentages[2][1]:
                lst.append(1)
        elif layer == 8:                            #If the measure is x/8 the kick can only append a whole, half, quarter or eight note (10/15/50/25)
            if rnd <= percentages[3][0]:
                lst.append(4)
            elif rnd > percentages[3][0] and rnd <= percentages[3][0]+percentages[3][1]:
                lst.append(2)
            elif rnd > percentages[3][0]+percentages[3][1] and rnd <= percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(1)
            elif rnd > percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(0.5)
        elif layer == 16:                           #If the measure is x/16 the kick can only append a whole, half, quayrter, eight or sixteenth note (7.5/12.5/20/40/20)
            if rnd <= percentages[4][0]:
                lst.append(4)
            elif rnd > percentages[4][0] and rnd <= percentages[4][0]+percentages[4][1]:
                lst.append(2)
            elif rnd > percentages[4][0]+percentages[4][1] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]:
                lst.append(1)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2] and rnd <= percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(0.5)
            elif rnd > percentages[4][0]+percentages[4][1]+percentages[4][2]+percentages[4][3]:
                lst.append(0.25)
        lst.reverse()                               #Get the last element
        pos += lst[0]                               #The measure will fill up according to the length of the generated note
        lst.reverse()                               #Put the value back at the end
    if pos > count:                                 #If list is overcounted check by how much and remove the difference
        dif = 0
        if offset <= 25:                            #25% chance there will be an offset for the kick
            offset = 0.5
            dif = (pos - count)+offset
            bitoff = True
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
    while count > 1:                                #Generate a list with as many loops as user defined
        shuffle(shuffledlst)
        lst = lst+shuffledlst
        count-=1
    oldtimeval = 0 + offset
    rhythm.insert(0,oldtimeval)
    for f in lst:
        oldtimeval+=f
        rhythm.append(oldtimeval)
    rhythm.pop()
    return rhythm

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
        print(rhythmKick)
        rhythmSnare = Gen(beatCount,oneBeatVal,rhythmSnare,2)
        print(rhythmSnare)
        rhythmHat = Gen(beatCount,oneBeatVal,rhythmHat,4)
        print(rhythmHat)
        timestampKick = convertToStamps(rhythmKick)
        timestampSnare = convertToStamps(rhythmSnare)
        timestampHat = convertToStamps(rhythmHat)
    else:
        time.sleep(0.001)
    print(timestampKick)
    print(timestampSnare)
    print(timestampHat)

beatGen(measure[0],measure[1])
