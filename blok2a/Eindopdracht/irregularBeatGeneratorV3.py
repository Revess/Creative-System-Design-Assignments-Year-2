##--Imports--##
import math
import random
import threading
import time
from random import shuffle
from threading import Thread

import simpleaudio as sa
from midiutil import MIDIFile
from pynput.keyboard import Controller, Key, Listener

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
channel = 0
timer = 0
velocity = 100
statedepth = -1
statestorage = []
keyboard = Controller()

##--Functions--##
def on_press(key):                                  #Do something if a key is pressed
    pass
def on_release(key):                                #Do something if key is released
    global statedepth, statestorage, command
    if key == Key.up:                               #When the up arrow is released it will scroll upwards in the code
        if len(statestorage) == 0:                  #Prevents code from breaking (When the list is empty)
            keyboard.type('')
        elif statedepth >= len(statestorage)-1:     #Prevents code from breaking (above highest possible)
            for stor in list(statestorage[statedepth]):     #First it will delete what has been written in the state
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            for stor in list(statestorage[statedepth]):     #Only type the highest stored value
                keyboard.type(str(stor))
        else:
            statedepth+=1
            for stor in list(statestorage[statedepth-1]):   #First it will delete what has been written in the state
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            for stor in list(statestorage[statedepth]):     #Then it will type what has last been written (jumps up in time)
                keyboard.type(str(stor))
    elif key == Key.down:                             #When the up arrow is released it will scroll downwards in the code
        if statedepth <= 0:                         #Prevents code from breaking (below lowest low fix)
            if statedepth >-1:
                statedepth = -1
            keyboard.type('')
        else:
            statedepth-=1
            for stor in list(statestorage[statedepth]):     #First it will delete what has been written in the state
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            for stor in list(statestorage[statedepth]):     #Then it will type what has last been written (jumps down in time)
                keyboard.type(str(stor))
    if command == 'exit()':
        return False

def isFloat(x):                                     #To check if a value is a floating point number, if it is not return false
    try:
        int(x)
        return False
    except ValueError:
        return True

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
    # print(timestampKick)
    # print(timestampSnare)
    # print(timestampHat)

def player(s,stamps):                                      #The same for every player only difference is the sample
    global timestampKick,timestampSnare,timestampHat, command
    while True:
        if stamps == 0:
            lst = timestampKick
        elif stamps == 1:
            lst = timestampSnare
        elif stamps == 2:
            lst = timestampHat
        if command == 'play' and len(lst) > 0:
            startTime = time.time()                 #Updates the start time every new loop
            pos = 1                                 #Tracker for the current position in the list
            length = len(lst)                       #The length of the list
            for ts in lst:                          #Walks us through the timestamps list
                while True:
                    currentTime = time.time()       #Update the current time for the coming equation
                    if(currentTime - startTime >= ts):
                        if pos == length:
                            playObject = samples[s].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            pos += 1
                            command = 'none'
                            break
                        elif command == 'stop' or command == 'exit()':
                            playObject = samples[s].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            break
                        elif command == 'pause':
                            playObject = samples[s].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            while command == 'pause':
                                time.sleep(0.001)
                            startTime=time.time() - (currentTime - startTime)   #Set the starttime to the new offset
                            break
                        else:
                            samples[s].play()       #Play the given sample out of the file
                            pos += 1
                            break
                if command == 'stop' or command == 'exit()':
                    break
        elif command == 'exit()':
            break
        else:
            time.sleep(0.001)

def writeToMidi():
    filename = 'beat.mid'
    MyMIDI = MIDIFile(2)                 #Om welk midifile het gaat
    MyMIDI.addTempo(track,timer,bpm)     #Om het tempo in te stellen
    MyMIDI.addTimeSignature(track,timer,int(measure[0]),int(math.log(int(measure[1]),2)),24)    #Timesignature heeft een track nummer nodig(0), een tijdplek (timer) om aan te geven waar de midi start (begint nu vanaf miditick 1),
                                                                                                #Daarnaast het aantal tellen in een maat (nu kan de user opgeven, maar bijvoorbeeld 4), de waarde van een tel uitgedrukt in een exponent(dus 3 =
                                                                                                #2^3= 8ste noot enz., en daarnaast het aantal clocks per tick. 24 in een kwartnoot.
    pos = 0
    for ts in timestampKick:
        MyMIDI.addNote(track,channel,36,2*ts,rhythmKick[pos],velocity)                          #Voeg een noot toe door de track, het midikanaal, nootnummer, de starttijd (dus de positie in het grid (2 keer de timestamp waarde)), nootlengte in ms en de velocity
        pos+=1
    pos = 0
    for ts in timestampSnare:
        MyMIDI.addNote(track,channel,39,2*ts,rhythmSnare[pos],velocity)
        pos+=1
    pos = 0
    for ts in timestampHat:
        MyMIDI.addNote(track,channel,42,2*ts,rhythmHat[pos],velocity)
        pos+=1
    with open(filename, 'wb') as output_file:
        MyMIDI.writeFile(output_file)                                                           #Schrijf het bestand uit
        print('Successfully exported the rhythm as: ' + str(filename))                          #Gwn een leuk print ding

##--Main--##
def main():
    global bpm, plays, rhythm_obj_lst, tempo, measure, command, timestampKick, timestampSnare, timestampHat, rhythmKick, rhythmSnare, rhythmHat, statedepth, statestorage
    state = ['main']
    length = 0
    print("Welcome to the irregular beat generator. Type 'help' to display all the available commands")
    while True:
        if state[0] == 'main':                      #The return back to give another command to the system
            statedepth = -1
            state = input('>>> ').lower().split()   #Make sure the userinput is lowercased and spit into an array (array ignores spaces)
            length = len(state)
            if not len(state) == 0:                 #Makes only if the input is filled with text
                string = ' '.join(state)            #Joins the list of input again with spaces
                statestorage.insert(0,string)       #Add the input string to the storage
            else:
                state = ['main']
        elif state[0] == 'help':                    #If the command of the user is "help" it can view the help file
            if length == 1:
                print('To view the options of each command type: "Help + [command]". \nThe commands are not case sensitive.')
                print('These are the commands you can use: \n-bpm           -continue\n-exit/exit()   -export/ex\n-generate/gen  -help\n-loop          -measure\n-pause         -play\n-stop          -view')
            elif length == 2:
                if state[1] == 'bpm':
                    print('With bpm you can set the bpm for the generated rhythm')
                    print('The command "bpm" accepts the following arguments: \n-The bpm you would like to use in whole numbers \nExample: bpm 120')
                elif state[1] == 'continue':
                    print('With continue you can continue a paused loop')
                elif state[1] == 'exit' or state[1] == 'exit()':
                    print('With exit or exit() you can exit the program safely')
                elif state[1] == 'export' or state[1] == 'ex':
                    print('With export or ex you can export the generated beat as a ".mid" file')
                elif state[1] == 'generate' or state[1] == 'gen':
                    print('With generate or gen you can generate a beat')
                elif state[1] == 'help':
                    print('With help you can read the help file')
                elif state[1] == 'loop':
                    print('With loop you can set how long the generated rhythm will be.')
                    print('The command "loop" accepts the following arguments: \n-To set the length type "length" followed by a whole number \nExample: loop length 5')
                elif state[1] == 'measure':
                    print('With measure you can set the measure for the generated rhythm')
                    print('The command "measure" accepts the following arguments: \n-Set the measure by typing the bar count and the one beat value divided by a "/" \nExample: measure 4/4')
                elif state[1] == 'pause':
                    print('With pause you can pause the current loop, continue it with the command conintue')
                elif state[1] == 'play':
                    print('With play you can play the generated loop')
                elif state[1] == 'stop':
                    print('With stop you can stop the current playing loop')
                elif state[1] == 'view':
                    print('With view you can view the current values for the commands')
                    print('The command "view" accepts the following arguments: \n-Bpm \n-Measure \n-loop \nExample: view bpm')
                else:
                    print('Invalid argument for command: "help"')
            state = ['main']
        elif state[0] == 'view':                    #If the command of the user is "view" it can view one of the memory states, still need to fix this
            success = False
            if length == 1:
                print('Missing argument')
                print('The command "view" accepts the following arguments: \n-bpm \n-measure \n-loop')
                success = True
            elif length == 2:
                if state[1] == 'bpm':
                    print('The current bpm has been set to: ' + str(bpm))
                    success = True
                elif state[1] == 'loop':
                    print('The current amount of loops has been set to: ' + str(plays))
                    success = True
                elif state[1] == 'measure':
                    print('The current measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
                    success = True
            if not success:
                print('Invalid argument for command: "view"')
                print('The command "view" accepts the following arguments: \n-bpm \n-measure \n-loop')
            state = ['main']
        elif state[0] == 'bpm':                     #If the command of the user is "bpm" it can set the bpm
            success = False
            if length == 1:
                print('Missing argument')
                print('Give bpm in whole numbers')
            elif length == 2:
                if isFloat(state[1]):
                    pass
                elif int(state[1]) > 0 and int(state[1]) < 999:
                    bpm = int(state[1])
                    tempo = 60/bpm
                    success = True
            if not success:
                if not length == 1:
                    print('Invalid argument for command: "bpm"')     
                    print('Give bpm in whole numbers')               
            else:
                print('The bpm has been successfully set to: ' + str(bpm))
            state = ['main']
        elif state[0] == 'loop':                    #If the state of the command is "loop" it can set the number of loops
            success = False
            if length == 1 or length == 2:
                print('Missing argument')
                print('Set the loop length giving the arguments: length + "length in whole numbers"')
            if length == 3:
                if not state[2].isdigit() or not state[1] == 'length':
                    pass
                elif int(state[2]) > 0 and int(state[2]) < 20:
                    plays = int(state[2])
                    success = True
            if not success:
                if length == 1 or length == 2:
                    pass
                else:
                    print('Invalid argument for command: "loop"')
                    print('Set the loop length giving the arguments: length + "length in whole numbers"')
            else:
                print('The number of loops has been set to: ' + str(plays))
            state = ['main']
        elif state[0] == 'measure' or state[0] == 'meas':                 #If the state of the command is "measure" it can set the measure of the beat
            success = False
            if length == 1:
                print('Missing argument')
                print('Give the wanted measure divided by a "/"')
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
                        success = True
            if not success:
                if not length == 1:
                    print('Invalid argument for command: "measure"')
                    print('Give the wanted measure divided by a "/"')
            else:
                print('The measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
            state = ['main']        
        elif state[0] == 'generate' or state[0] == 'gen':                #Generate the beat
            command = 'generate'
            beatGen(measure[0],measure[1])
            print("Successfully generated the beat")
            state = ['main']
        elif state[0] == 'play':                    #Play the beat
            command = 'stop'
            time.sleep(1)
            command = 'play'
            state = ['main']
        elif state[0] == 'stop':                    #Stop the beat from playing
            command = 'stop'
            state = ['main']
        elif state[0] == 'pause':                    #Pause the beat from playing
            command = 'pause'
            state = ['main']
        elif state[0] == 'continue':
            command = 'continue'
            state = ['main']
        elif state[0] == 'exit()' or state[0] == 'exit':    #Exit the program
            command = 'exit()'
            break
        elif state[0] == 'export' or state[0] == 'ex':
            writeToMidi()
            state = ['main']
        else:                                       #If the command is unknown
            print('Unknown command, type "help" to see the full list of commands')
            state = ['main']

if __name__ == '__main__':
    t1 = Thread(target=main)
    t2 = Thread(target=player, args=(2,0))          #The Kick playing thread
    t3 = Thread(target=player, args=(1,1))          #The Snare playing thread
    t4 = Thread(target=player, args=(6,2))          #The Hat playing thread

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    with Listener(                                  #Start the listener function Thread (baked into pynput library)
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

print("Successfully closed the program")
