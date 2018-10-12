##--Imports--##
import simpleaudio as sa
import time
import random

##--Objects--##
samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav"),sa.WaveObject.from_wave_file("./audioFiles/snare.wav"),sa.WaveObject.from_wave_file("./audioFiles/SecretKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/RoninKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/PrydaSnare.wav"),sa.WaveObject.from_wave_file("./audioFiles/Hard.wav")]
bpm = 120
tempo = 60 / bpm
timestamps = [0]
rhythm = []
rhythm_obj_lst = [1, 2, 4 ,8 ,16]
timestamps = []
plays = 0
measure = ['4', '4']

##--Functions--##
def isFloat(x):
    try:
        int(x)
        return False
    except ValueError:
        return True

def convertToStamps(lst):
    global plays
    stamps = []
    ms_lst = lst
    x = 0                                           #The old timestamp value is x
    stamps.insert(0,0)                              #Make the starting sample start on timestamp 0
    while plays > 0:                                #If we still didn't get to the end of the requested amount of loops repeat
        for f in ms_lst:                            #For every floatingpoint number in the milisecond list
            x += f                                  #Add the current floatingpoint to the previous one, the new timestamp is created
            stamps.append(x)                        #Add this timestamp to the list
        plays -= 1                                  #One loop is compleated substract one
        shuffleLst(ms_lst)                          #Mix the old rhythm playlist so we can generate more random lists (See the function for explanation)
    stamps.pop()                                    #Remove the last stamp to so the offset we created at the start (insert a 0) works right
    return stamps

def player(lst):                                    #Need to make sure this function can play three samples at once
    global plays, timestamps, rhythm
    startTime = time.time()                         #Updates the start time every new loop
    x = 1                                           #Tracker for the current position in the list
    length = len(lst)                               #The length of the list
    lngth = len(samples)                            #Length of the sample list
    for ts in lst:                                  #Walks us through the timestamps list
        while True:
            currentTime = time.time()               #Update the current time for the coming equation
            if(currentTime - startTime >= ts):
                rnd = round(((lngth-1)*random.random()))    #Generate a random string to play a random sample out of the files
                if x == length:
                    playObject = samples[rnd].play()        #Create a playObject so the last sample will be played fully
                    playObject.wait_done()
                    x += 1
                    break
                else:
                    samples[rnd].play()             #Play the given sample out of the file
                    x += 1
                    break
    print("Done playing")

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

def beatGen():
    #Need to create precentages for the kick snare and hi-hat and 
    return

def convertToMidi():
    return

##--Main--##
def main():
    global bpm, plays, rhythm_obj_lst, measure
    state = ['main']
    length = 0
    print("Welcome to the irregular beat generator. Type help to display all the available commands")
    while True:
        if state[0] == 'main':                      #The return back to give another command to the system
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
                if state[0] == 'back':
                    break
                elif length == 1:
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
                            bpm = state[0]
                            succes = True
                            break
                elif length == 2:
                    if not state[1].isdigit:
                        print('Invalid argument')
                    elif isFloat(state[1]):
                        print('BPM does not accept floats')
                    elif int(state[1]) > 0 and int(state[1]) < 999:
                        bpm = state[1]
                        succes = True
                if not succes:
                    print('Invalid argument for command: "bpm')
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
                            plays = state[0]
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
                                plays = state[0]
                                succes = True
                                break
                            else:
                                print('Invalid argment')
                elif state[0] == 'back':
                    break
                if not succes:
                    if not state[0] == 'back':
                        if length == 3:
                            if not state[2].isdigit() or not state[1] == 'length':
                                print('Invalid argument(s) for command: "loop"')
                                break
                            elif int(state[2]) > 0 and int(state[2]) < 20:
                                plays = state[2]
                                succes = True
                        else:
                            print('Invalid argument for command: "loop"')
                            break
                    else:
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
                elif state[0] == 'back':
                    break
                if not succes:
                    if not state[0] == 'back': 
                            print('Invalid argument for command: "measure"')
                            break
                    else:
                        break
                else:
                    print('The measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
                    break
            state = ['main']
        else:                                       #If the command is unkown
            print('Unkown command, type "help" to see the full list of commands')
            state = ['main']
main()

##Helpfile: None of the arguments or the commands are case sensitive. 
# If only command is typen the user will be asked for arguments
# -Loop, uses argument length, length needs a number. Example: Loop length 10
# -Measure, uses argument "measure type". Example: Measure 4/4
# -BPM, uses argument "tempo number". Example: BPM 120
