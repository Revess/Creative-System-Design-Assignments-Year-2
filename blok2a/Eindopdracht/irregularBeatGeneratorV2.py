##--Imports--##
import simpleaudio as sa
import random
import time
from random import shuffle
import threading
from threading import Thread
import midiutil
from midiutil import MIDIFile
import math

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
track = 0
channel = 9
timer = 0
velocity = 100

##--Functions--##
def isFloat(x):                                     #To check if a value is a floating point number, if it is not return false
    try:
        int(x)
        return False
    except ValueError:
        return True

def convertToStamps(lst):                           #Convert a list to timestamps
    count = plays
    stamps = []
    ms_lst = lst
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
            if rnd <= percentages[1][0]:
                lst.append(1)
            elif rnd > percentages[1][1]:
                lst.append(2)
        elif val == 4:                              #If the measure is x/4 the kick can only append a whole, half or quarter note (10/60/30)
            if rnd <= percentages[2][0]:
                lst.append(1)
            elif rnd > percentages[2][0] and rnd <= percentages[2][0]+percentages[2][1]:
                lst.append(2)
            elif rnd > percentages[2][0]+percentages[2][1]:
                lst.append(4)
        elif val == 8:                              #If the measure is x/8 the kick can only append a whole, half, quarter or eight note (10/15/50/25)
            if rnd <= percentages[3][0]:
                lst.append(1)
            elif rnd > percentages[3][0] and rnd <= percentages[3][0]+percentages[3][1]:
                lst.append(2)
            elif rnd > percentages[3][0]+percentages[3][1] and rnd <= percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(4)
            elif rnd > percentages[3][0]+percentages[3][1]+percentages[3][2]:
                lst.append(8)
        elif val == 16:                             #If the measure is x/16 the kick can only append a whole, half, quarter, eight or sixteenth note (7.5/12.5/20/40/20)
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
            state = input('>>> ').lower().split()
            length = len(state)
        elif state[0] == 'help':                    #If the command of the user is "help" it can view the help file
            if length == 1:
                print('To view the options of each command type: "Help + [command]". \nThe commands are not case sensitive.')
                print('These are the commands you can use: \nbpm        exit/exit() \ngenerate   loop \nmeasure    play \nstop       view')
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
            if length == 1:
                print('Missing argument')
                print('The command "view" accepts the following arguments: \n-bpm \n-measure \n-loop')
                succes = True
            elif length == 2:
                if state[1] == 'bpm':
                    print('The current bpm has been set to: ' + str(bpm))
                    succes = True
                elif state[1] == 'loop':
                    print('The current amount of loops has been set to: ' + str(plays))
                    succes = True
                elif state[1] == 'measure':
                    print('The current measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
                    succes = True
            if not succes:
                print('Invalid argument for command: "view"')
                print('The command "view" accepts the following arguments: \n-bpm \n-measure \n-loop')
            state = ['main']
        elif state[0] == 'bpm':                     #If the command of the user is "bpm" it can set the bpm
            succes = False
            if length == 1:
                print('Missing argument')
                print('Give bpm in whole numbers')
            elif length == 2:
                if isFloat(state[1]):
                    pass
                elif int(state[1]) > 0 and int(state[1]) < 999:
                    bpm = int(state[1])
                    tempo = 60/bpm
                    succes = True
            if not succes:
                if not length == 1:
                    print('Invalid argument for command: "bpm"')     
                    print('Give bpm in whole numbers')               
            else:
                print('The bpm has been succesfully set to: ' + str(bpm))
            state = ['main']
        elif state[0] == 'loop':                    #If the state of the command is "loop" it can set the number of loops
            succes = False
            if length == 1 or length == 2:
                print('Missing argument')
                print('Set the loop length giving the arguments: length + "length in whole numbers"')
            if length == 3:
                if not state[2].isdigit() or not state[1] == 'length':
                    pass
                elif int(state[2]) > 0 and int(state[2]) < 20:
                    plays = int(state[2])
                    succes = True
            if not succes:
                if length == 1 or length == 2:
                    pass
                else:
                    print('Invalid argument for command: "loop"')
                    print('Set the loop length giving the arguments: length + "length in whole numbers"')
            else:
                print('The number of loops has been set to: ' + str(plays))
            state = ['main']
        elif state[0] == 'measure':                 #If the state of the command is "measure" it can set the measure of the beat
            succes = False
            if length == 1:
                print('Missing argument')
                print('Give the wanted measure devided by a "/"')
            elif length == 2:
                state = state[1].split('/')
                state = [x for x in state if x]
                if len(state) > 2:
                    pass
                elif isFloat(state[0]) or isFloat(state[1]):
                    pass
                elif int(state[0]) < 20:
                    for x in rhythm_obj_lst:
                        if x == int(state[1]):
                            measure = state.copy()
                    if len(measure) > 0:
                        succes = True
            if not succes:
                if not length == 1:
                    print('Invalid argument for command: "measure"')
                    print('Give the wanted measure devided by a "/"')
            else:
                print('The measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
            state = ['main']        
        elif state[0] == 'generate':                #Generate the beat
            command = 'generate'
            beatGen(measure[0],measure[1])
            print("Succesfully generated the beat")
            state = ['main']
        elif state[0] == 'play':                    #Play the beat
            command = 'play'
            state = ['main']
        elif state[0] == 'stop':                    #Stop the beat from playing
            command = 'stop'
            state = ['main']
        elif state[0] == 'exit()' or state[0] == 'exit':    #Exit the program
            command = 'exit()'
            break
        else:                                       #If the command is unkown
            print('Unkown command, type "help" to see the full list of commands')
            state = ['main']

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

print("Succesfully closed the program")