##--Imports--##
import simpleaudio as sa
import random
<<<<<<< HEAD
import time
from random import shuffle
import threading
from threading import Thread
import midiutil
from midiutil import MIDIFile
import math
=======
from random import shuffle
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6

##--Objects--##
samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav"),sa.WaveObject.from_wave_file("./audioFiles/snare.wav"),sa.WaveObject.from_wave_file("./audioFiles/SecretKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/RoninKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/PrydaSnare.wav"),sa.WaveObject.from_wave_file("./audioFiles/Hard.wav"), sa.WaveObject.from_wave_file("./audioFiles/Hat_Closed_2.wav")]
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
measure = ['4', '4']
command = ''
percentages = [100,[50,50],[10,60,30],[10,15,50,25],[7.5,12.5,20,40,20]]
<<<<<<< HEAD
track = 0
channel = 9
timer = 0
velocity = 100
=======
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6

##--Functions--##
def isFloat(x):                                     #To check if a value is a floating point number, if it is not return false
    try:
        int(x)
        return False
    except ValueError:
        return True

<<<<<<< HEAD
def convertToStamps(lst):                           #Convert a list to timestamps
    count = plays
    stamps = []
    ms_lst = lst
=======
def convertToStamps(lst):
    global plays
    count = plays
    stamps = []
    ms_lst = lst
    print(ms_lst)
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
    offset = ms_lst.pop()
    x = 0 + offset                                  #The old timestamp value is x
    stamps.insert(0,x)                              #Make the starting sample start on timestamp 0
    while count > 0:                                #If we still didn't get to the end of the requested amount of loops repeat
        for f in ms_lst:                            #For every floatingpoint number in the milisecond list
            x += f                                  #Add the current floatingpoint to the previous one, the new timestamp is created
            stamps.append(x)                        #Add this timestamp to the list
        count -= 1                                  #One loop is compleated substract one
        shuffle(ms_lst)                             #Mix the old rhythm playlist so we can generate more random lists (See the function for explanation)
    stamps.pop()                                    #Remove the last stamp to so the offset we created at the start (insert a 0) works right
    return stamps

<<<<<<< HEAD
def lowGen(count,val,lst):                          #This works the same for every layer of generation
    global percentages,tempo
    count = count*(tempo/(val/val))                 #Transforms the musical terminoligy to floating point numbers in miliseconds according to the BPM. 
                                                    #7/4 with a bpm of 120 will make it 3.5/4, because one quarter note will be 0.5ms there will fit 7 quarter notes in one measure
    pos = 0                                         #Tracks the position of how long one measure will be
    offset = 100*random.random()                    #Create random value for the offset chance
    bitoff = False                                  #Offset is set to 0 right now
    while count > pos:
        rnd = 100*random.random()
        if val == 1:                                #If the measure is x/1 the kick can only append a whole note
            lst.append(1)
        elif val == 2:                              #If the measure is x/2 the kick can only append a whole or half note (50/50)
=======
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
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
            if rnd <= percentages[1][0]:
                lst.append(1)
            elif rnd > percentages[1][1]:
                lst.append(2)
<<<<<<< HEAD
        elif val == 4:                              #If the measure is x/4 the kick can only append a whole, half or quarter note (10/60/30)
=======
        elif val == 4:
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
            if rnd <= percentages[2][0]:
                lst.append(1)
            elif rnd > percentages[2][0] and rnd <= percentages[2][0]+percentages[2][1]:
                lst.append(2)
            elif rnd > percentages[2][0]+percentages[2][1]:
                lst.append(4)
<<<<<<< HEAD
        elif val == 8:                              #If the measure is x/8 the kick can only append a whole, half, quarter or eight note (10/15/50/25)
=======
        elif val == 8:
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
            if rnd <= percentages[3][0]:
                lst.append(1)
            elif rnd > percentages[3][0] and rnd <= percentages[3][0]+percentages[3][1]:
                lst.append(2)
            elif rnd > percentages[3][0]+percentages[3][1] and rnd <= percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(4)
            elif rnd > percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(8)
<<<<<<< HEAD
        elif val == 16:                             #If the measure is x/16 the kick can only append a whole, half, quarter, eight or sixteenth note (7.5/12.5/20/40/20)
=======
        elif val == 16:
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
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
<<<<<<< HEAD
        lst.reverse()                               #Get the last element
        lst[0]/=val                                 #Transform the note to floatingpoint in ratio
        lst[0]=tempo/lst[0]                         #Transform to miliseconds
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
    lst.append(offset)                              #Add the offset at the end for the timestamp calculations
=======
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
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
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
        lowGen(beatCount,oneBeatVal,rhythmKick)
        midGen(beatCount,oneBeatVal,rhythmSnare)
        highGen(beatCount,oneBeatVal,rhythmHat)
        timestampKick = convertToStamps(rhythmKick)
        timestampSnare = convertToStamps(rhythmSnare)
        timestampHat = convertToStamps(rhythmHat)
    else:
        time.sleep(0.001)
    # print(timestampKick)
    # print(timestampSnare)
    # print(timestampHat)

def playLow():                                      #The same for every player only difference is the sample
    global timestampKick, command
    while True:
        lst = timestampKick
        if command == 'play':
            startTime = time.time()                 #Updates the start time every new loop
            x = 1                                   #Tracker for the current position in the list
            length = len(lst)                       #The length of the list
            for ts in lst:                          #Walks us through the timestamps list
                while True:
                    currentTime = time.time()       #Update the current time for the coming equation
                    if(currentTime - startTime >= ts):
                        if x == length or command == 'stop' or command == 'exit()':
                            playObject = samples[2].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            x += 1
                            command = 'none'
                            break
                        else:
                            samples[2].play()       #Play the given sample out of the file
                            x += 1
                            break
        elif command == 'exit()':
            break
        else:
            time.sleep(0.001)

def playMid():
    global timestampSnare, command
    while True:
        lst = timestampSnare
        if command == 'play':
            startTime = time.time()                         #Updates the start time every new loop
            x = 1                                           #Tracker for the current position in the list
            length = len(lst)                               #The length of the list
            for ts in lst:                                  #Walks us through the timestamps list
                while True:
                    currentTime = time.time()               #Update the current time for the coming equation
                    if(currentTime - startTime >= ts):
                        if x == length or command == 'stop' or command == 'exit()':
                            playObject = samples[1].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            x += 1
                            command = 'none'
                            break
                        else:
                            samples[1].play()             #Play the given sample out of the file
                            x += 1
                            break
        elif command == 'exit()':
            break
        else:
            time.sleep(0.001)

def playHigh():
    global timestampHat, command
    while True:
        lst = timestampHat
        if command == 'play':
            startTime = time.time()                         #Updates the start time every new loop
            x = 1                                           #Tracker for the current position in the list
            length = len(lst)                               #The length of the list
            for ts in lst:                                  #Walks us through the timestamps list
                while True:
                    currentTime = time.time()               #Update the current time for the coming equation
                    if(currentTime - startTime >= ts):
                        if x == length or command == 'stop' or command == 'exit()':
                            playObject = samples[6].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            x += 1
                            command = 'none'
                            break
                        else:
                            samples[6].play()             #Play the given sample out of the file
                            x += 1
                            break
        elif command == 'exit()':
            break
        else:
            time.sleep(0.001)

def writeToMidi():
    MyMIDI = MIDIFile(2)
    MyMIDI.addTempo(track,timer,bpm)
    MyMIDI.addTimeSignature(track,timer,measure[0],math.log(measure[1],2),24)

##--Main--##
def main():
    global bpm, plays, rhythm_obj_lst, tempo, measure, command, timestampKick, timestampSnare, timestampHat, rhythmKick, rhythmSnare, rhythmHat
    state = ['main']
    length = 0
    print("Welcome to the irregular beat generator. Type 'help' to display all the available commands")
    while True:
        if state[0] == 'main':                      #The return back to give another command to the system
            command = 'none'
            state = input('>>> ').lower().split()
            length = len(state)
        elif state[0] == 'help':                    #If the command of the user is "help" it can view the help file
            if length == 1:
                print('To view the options of each command type: "Help [command]". \nThe commands are not case sensitive.')
                print('These are the commands you can use: \nbpm       help \nloop      measure \nview ')
            elif length == 2:
                if state[1] == 'bpm':
                    print('With bpm you can set the bpm for the generated rhythm')
                    print('The command "bpm" accepts the following arguments: \n-The bpm you would like to use in whole numbers \nExample: bpm 120')
                elif state[1] == 'loop':
                    print('With loop you can set how long the generated rhythm will be.')
                    print('The command "loop" accepts the following arguments: \n-To set the length type "length" followed by a whole number \nExample: loop length 5')
                elif state[1] == 'measure':
                    print('With measure you can set the measur for the generated rhythm')
                    print('The command "measure" accepts the following arguments: \n-Set the measure by typing the bar count and the one beat value divided by a "/" \nExample: measure 4/4')
                elif state[1] == 'view':
                    print('With view you can view the current values for the commands')
                    print('The command "view" accepts the following arguments: \n-Bpm \n-Measure \n-loop \nExample: view bpm')
                else:
                    print('Invalid argument for command: "help"')
            state = ['main']
        elif state[0] == 'view':                    #If the command of the user is "view" it can view one of the memory states, still need to fix this
            succes = False
            while True:
                if length == 1:
                    while True:
                        state = [input('Which variable would you like to view? \n>>> ').lower()]
                        state = state[0].split()
                        statelength = len(state) 
                        if state[0] == 'bpm':
                            print('The current bpm has been set to: ' + str(bpm))
                            succes = True
                            break
                        elif state[0] == 'loop':
                            print('The current amount of loops has been set to: ' + str(plays))
                            succes = True
                            break
                        elif state[0] == 'measure':
                            print('The current measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
                            succes = True
                            break
                        else:
                            print('Invalid argument')
                elif length == 2:
                    if state[1] == 'bpm':
                        print('The current bpm has been set to: ' + str(bpm))
                        succes = True
                        break
                    elif state[1] == 'loop':
                        print('The current amount of loops has been set to: ' + str(plays))
                        succes = True
                        break
                    elif state[1] == 'measure':
                        print('The current measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
                        succes = True
                        break
                if not succes:
                    print('Invalid argument for command: "view"')
                    break
                else:
                    break
            state = ['main']
        elif state[0] == 'bpm':                     #If the command of the user is "bpm" it can set the bpm
            succes = False
            while True:
                if length == 1:
                    while True:
                        state = [input('What BPM would you like to use? \n>>> ').lower()]
                        state = state[0].split()
                        statelength = len(state)
                        if state[0] == 'back':
                            break
                        elif statelength > 1:
                            print("Too many arguments given")
                        elif statelength < 1:
                            print("Not enough arguments given")
                        elif not state[0].isdigit:
                            print('Invalid argument')
                        elif isFloat(state[0]):
                            print('BPM does not accept floats')
                        elif int(state[0]) > 0 and int(state[0]) < 999:
                            bpm = int(state[0])
<<<<<<< HEAD
                            tempo = 60/bpm
=======
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
                            succes = True
                            break
                elif length == 2:
                    if not state[1].isdigit:
                        print('Invalid argument')
                    elif isFloat(state[1]):
                        print('BPM does not accept floats')
                    elif int(state[1]) > 0 and int(state[1]) < 999:
                        bpm = int(state[1])
<<<<<<< HEAD
                        tempo = 60/bpm
=======
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
                        succes = True
                if not succes:
                    if state[0] == 'back':
                        print('You returned to the main menu')
                        break
                    else:
                        print('Invalid argument for command: "bpm"')
                        break
                else:
                    print('The bpm has been succesfully set to: ' + str(bpm))
                    break
            state = ['main']
        elif state[0] == 'loop':                    #If the state of the command is "loop" it can set the number of loops
            succes = False
            while True:
                if length == 1:
                    while True:
                        state = [input('How many bars should the rhythm be? \n>>> '.lower())]
                        state = state[0].split()
                        statelength = len(state)
                        if state[0] == 'back':
                            break
                        elif statelength > 1:
                            print("Too many arguments given")
                        elif statelength < 1:
                            print("Not enough arguments given")
                        elif not state[0].isdigit():
                            print('Invalid argument')
                        elif isFloat(state[0]):
                            print("Loop does not accept floats")
                        elif int(state[0]) > 0 and int(state[0]) < 20:
                            plays = int(state[0])
                            succes = True
                            break
                        else:
                            print('Invalid argument')
                elif length == 2:
                    if state[1] == 'length':
                        while True:
                            state = [input('How many bars should the rhythm be? \n>>> '.lower())]
                            if state[0] == 'back':
                                break
                            elif not state[0].isdigit():
                                print('Invalid argument')
                            elif isFloat(state[0]):
                                print("Loop does not accept floats")
                            elif int(state[0]) > 0 and int(state[0]) < 20:
                                plays = int(state[0])
                                succes = True
                                break
                            else:
                                print('Invalid argment')
                if not succes:
                    if not state[0] == 'back':
                        if length == 3:
                            if not state[2].isdigit() or not state[1] == 'length':
                                print('Invalid argument(s) for command: "loop"')
                                break
                            elif int(state[2]) > 0 and int(state[2]) < 20:
                                plays = int(state[2])
                                succes = True
                        else:
                            print('Invalid argument for command: "loop"')
                            break
                    else:
                        print('You returned to the main menu')
                        break
                else:
                    print('The number of loops has been set to: ' + str(plays))
                    break
            state = ['main']
        elif state[0] == 'measure':                 #If the state of the command is "measure" it can set the measure of the beat
            succes = False
            measure = []
            while True:
                if length == 1:
                    while True:
                        state = [input('In what measure whould I play the rhythm? \n>>> ').lower()]
                        state = state[0].split('/')
                        state = [x for x in state if x]
                        statelength = len(state)
                        if state[0] == 'back':
                            break
                        elif statelength <= 1:
                            print("Not enough arguments given")
                        elif statelength > 2:
                            print("Too many arguments given")
                        elif not state[0].isdigit or not state[1].isdigit:
                            print('Invalid argument')
                        elif isFloat(state[0]) or isFloat(state[1]):
                            print("Measure does not accept floats")
                        elif int(state[0]) < 20:
                            for x in rhythm_obj_lst:
                                if x == int(state[1]):
                                    measure = state.copy()
                            if len(measure) > 0:
                                succes = True
                                break
                            else:
                                break
                elif length == 2:
                    while True:
                        state = state[1].split('/')
                        state = [x for x in state if x]
                        statelength = len(state)
                        if state[0] == 'back':
                            break
                        elif statelength <= 1:
                            break
                        elif statelength > 2:
                            break
                        elif not state[0].isdigit or not state[1].isdigit:
                            print('Invalid argument')
                        elif isFloat(state[0]):
                            print("Measure does not accept floats")
                        elif int(state[0]) < 20:
                            for x in rhythm_obj_lst:
                                if x == int(state[1]):
                                    measure = state.copy()
                            if len(measure) > 0:
                                succes = True
                                break
                            else:
                                break
                if not succes:
                    if not state[0] == 'back': 
                            print('Invalid argument for command: "measure"')
                            break
                    else:
                        print('You returned to the main menu')
                        break
                else:
                    print('The measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
                    break
            state = ['main']        
        elif state[0] == 'generate':
            command = 'generate'
            beatGen(measure[0],measure[1])
<<<<<<< HEAD
            print("Succesfully generated the beat")
            state = ['main']
        elif state[0] == 'play':
            command = 'play'
=======
            state = ['main']
        elif state[0] == 'play':
            playHigh()
            playLow()
            playMid()
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
            state = ['main']
        elif state[0] == 'stop':
            command = 'stop'
            state = ['main']
        elif state[0] == 'exit()' or 'exit':
            command = 'exit()'
            break
        else:                                       #If the command is unkown
            print('Unkown command, type "help" to see the full list of commands')
            state = ['main']
<<<<<<< HEAD

if __name__ == '__main__':
    t1 = Thread(target=main)
    t2 = Thread(target=playHigh)
    t3 = Thread(target=playMid)
    t4 = Thread(target=playLow)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

print("Succesfully done program closing")
=======
main()
>>>>>>> ba24dde77ecdfffedc819744e94cc64bb78aaea6
