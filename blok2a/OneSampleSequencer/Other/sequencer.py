##--Imports--##
import simpleaudio as sa
import time
import random

##--Objects--##
samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav")]
bpm = 120
tempo = 60 / bpm
keepPlaying = True
firstRun = True
timestamps = [0]
rhythm = []
rhythm_obj_lst = [1, 2, 4 ,8 ,16]
timestamps = []
plays = 0

##--Functions--##
#Convert a rhythm string to timestamps
def convert(string):
    stamps = []
    a = 0
    ms_lst = []
    str_lst = string.split()
    float_lst = [float(i) for i in str_lst]
    for i in float_lst:                         #Convert the given list to the miliseconds by comparing the given values to the rhythm list
        for x in rhythm_obj_lst:
            if i == x:
                i = i/4                         #Brings the notes back to whole numbers (4 = quarter. 4/4 = 1. 8 = eight. 8/4 = 2 etc.)
                i = tempo/i                     #Over here the tempo will be devided by the number, so quarter will be 0.5, an eigth (tempo/2) will be 0.25
                ms_lst.append(i)                #Add them to a new list
    ms_lst.insert(0, a)                         #Append a 0 to the list to make sure first sample always starts right at the beginning
    p = 1
    x = 0
    for i in ms_lst:                            #Convert the milisecond list to a timestamp list by adding them together in seperate spaces
        if i == 0:
            stamps.append(i)
            p += 1
        elif p <= len(ms_lst)-1:
            x += i
            stamps.append(x)
            p += 1
    print(stamps)
    return stamps

#Play the given list
def player(lst):
    global keepPlaying, plays
    keepPlaying = True                          #Keeps the loop going until done
    while keepPlaying:
        if plays > 0:                           #Checks if the loop has to stop
            startTime = time.time()             #Updates the start time every new loop
            for ts in lst:                      #Walks us through the timestamps list
                while True:
                    currentTime = time.time()   #Update the current time for the coming equation
                    if(currentTime - startTime >= ts):
                        samples[0].play()       #Play the given sample out of the file
                        break                   #When the sample is played the update will set to false, this way the next time stamp will be used
                    else:
                        time.sleep(0.001)
            plays -= 1                          #Substract one from the asked loops
        elif plays <= 0:                        #if previous statement doesn't go in effect this one will stop the loop
            keepPlaying = False
    print("Done playing")      

##--Main--##
def main():
    global bpm, tempo, rhythm, timestamps, plays
    bpm = float(input("What bpm would you like to use? \n>>> "))
    tempo = 60 / bpm
    rhythm = convert(input("What rhythm would you like to play? \n>>> "))
    plays = int(input("How many times would you like the rhythm to be played? \n>>> "))
    timestamps = rhythm.copy()
    player(timestamps)
main()