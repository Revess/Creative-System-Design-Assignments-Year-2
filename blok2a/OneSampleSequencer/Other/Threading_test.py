import simpleaudio as sa
import threading
from threading import Thread
import time

#----Objects----#
#Machine on or off
running = True
#State of machine
state = 'main'
#Path to file
filePath = "../audioFiles/CowBell.wav"
#Bpm in ms
bpm = 0.5
#Amount of playtimes
numOfPlays = 5
#List of possible rhythms
rhythm_obj_lst = [1, 2, 4 ,8 ,16]
#List that contains the rhythm
rhythm_lst = [1, 1, 1, 1,]
#Timestamps
timestamps = [0, 0.5, 1.0 ,1.5]
#playerState
playerState = 'pause'
#The time of starting the code
startTime = time.time()
#Object file_path
samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav")]
#When started will it keep playing?
keepPlaying = True

#----Functions----#
def playFile():
    samples[0].play()

def converter(lst):
    stamps = []
    ms_lst = []
    str_lst = lst.split()
    for i in str_lst:
        if i == '|':
            str_lst.remove(i)
    float_lst = [float(i) for i in str_lst]
    for i in float_lst:
        for x in rhythm_obj_lst:
            if i == x:
                i = i/4
                i = bpm/i
                ms_lst.append(i)
    prev = -ms_lst[0]
    for i in ms_lst:
        stamps.append(i + prev)
        prev += i
    return stamps

def play():
    global playerState
    global startTime
    global keepPlaying
    timestamps_lst = timestamps
    timestamp = timestamps_lst.pop(0)
    while keepPlaying:
        if playerState == 'play':
            currentTime = time.time()
            if(currentTime - startTime >= timestamp):
                # play sample
                playFile()
                if playerState == 'playOnce':
                    if timestamps:
                        timestamp = timestamps.pop(0)
                    else:
                        keepPlaying = False
                if playerState == 'stop':
                    keepPlaying = False
                while playerState == 'pause':
                    time.sleep(0.001)
            else:
                time.sleep(0.001)  

def stating():
    global running, state, filePath, bpm, numOfPlays, rhythm_lst, rhythm_obj_lst, playerState, timestamps
    #Loop#
    while running:
    ####Setup####
        if state == 'main':
            state = input(">> ")

    ####Fundamentals####
    #---Help
        elif state == 'help':
            print("The following commands can be used: \ncurrentFile   play \nexit()        rhythm \ngetFile       tempo \nhelp          testFile \nnumOfPlays    testSequencer")
            state = 'main'

    ####Commands####
    ##----currentFile----##
        elif state == 'currentFile':
            print(filePath)
            state = 'main'
    ##----play----##
        elif state == 'play':
            print("Also try: playOnce, stop and pause")
            playerState = 'play'
            state = 'main'
    ##----playOnce----##
        elif state == 'playOnce':
            playerState = 'playOnce'
            state = 'main'
    ##----stop----##
        elif state == 'stop':
            playerState = 'stop'
            state = 'main'
    ##----pause----##
        elif state == 'pause':
            playerState = 'pause'
            state = 'main'
    ##----rhythm----##
        elif state == 'rhythm':
            print("Would you like to view or create the rhythm?")
            state = input(">>> ")
            if state == 'view':
                print("The current rhythmSequence is: " + str(rhythm_lst))
                state = 'main'
            elif state == 'create':
                print("Give your desired rhythm: ")
                rhythm_lst = []
                timestamps = []
                rhythm_lst = input(">>> ")
                timestamps = converter(rhythm_lst)
                state = 'main'
            else:
                state = 'main'
    ##----getFile----##
        elif state == 'getFile':
            filePath = input(">>> ")
            state = 'main'
    ##----tempo----##
        elif state == 'tempo':
            print("Would you like to view or set the tempo?")
            state = input(">>> ")
            if state == 'view':
                print("The current tempo is set to " + str(60/bpm) + " BPM")
                state = 'main'
            elif state == 'set':
                print("Give your desired tempo in BPM:")
                bpm = float(input(">>> "))
                print("The current tempo has been set to " + str(bpm) + " BPM")
                bpm = 60/bpm
                state = 'main'
    ##----testFile----##
        elif state == 'testFile':
            print("Starting file")
            playFile()
            print("Done playing")
            state = 'main'
    ##----numOfPlays----##
        elif state == 'numOfPlays':
            numOfPlays = int(input(">>> "))
            if numOfPlays > 20:
                print("This number is too high")
            else:
                state = 'main'
    #---Exit message to exit program
        elif state == 'exit()':
            exit()
    #---Invalid input
        else:
            print("Unkown command, to see the full list of commands use help")
            state = 'main'
    
if __name__ == '__main__':
    Thread(target = stating).start()
    Thread(target = play).start()