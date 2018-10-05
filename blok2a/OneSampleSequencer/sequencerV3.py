##--Imports--##
import simpleaudio as sa
import time
import random

##--Objects--##
samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav"),sa.WaveObject.from_wave_file("./audioFiles/snare.wav"),sa.WaveObject.from_wave_file("./audioFiles/SecretKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/RoninKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/PrydaSnare.wav"),sa.WaveObject.from_wave_file("./audioFiles/Hard.wav")]
bpm = 120
hard = 5
tempo = 60 / bpm
keepPlaying = True
firstRun = True
timestamps = [0]
rhythm = []
rhythm_obj_lst = [1, 2, 4 ,8 ,16]
timestamps = []
plays = 0
run = True

##--Functions--##
#Convert a string to a rhythm
def convertToMs(string):
    ms_lst = []
    str_lst = string.split()
    float_lst = [float(i) for i in str_lst]
    for i in float_lst:                         #Convert the given list to the miliseconds by comparing the given values to the rhythm list
        for x in rhythm_obj_lst:
            if i == x:
                i = i/4                         #Brings the notes back to whole numbers (4 = quarter. 4/4 = 1. 8 = eight. 8/4 = 2 etc.)
                i = tempo/i                     #Over here the tempo will be devided by the number, so quarter will be 0.5, an eigth (tempo/2) will be 0.25.
                ms_lst.append(i)                #Add them to a new list
    return ms_lst

#Convert a rhythm list to a timestamp list
def convertToStamps(lst):
    global run, plays
    stamps = []
    ms_lst = lst
    p = 0
    x = 0
    stamps.insert(0,0)
    while plays > 0:
        for f in ms_lst:                            #Convert the milisecond list to a timestamp list by adding them together in seperate spaces
            x += f
            stamps.append(x)
            p += 1
        plays -= 1
        shuffle_lst(ms_lst)
    stamps.pop()
    return stamps

#Play the given list
def player(lst):
    global keepPlaying, plays, timestamps, rhythm
    keepPlaying = True                          #Keeps the loop going until done
    startTime = time.time()             #Updates the start time every new loop
    x = 1
    length = len(lst)
    lngth = len(samples)
    for ts in lst:                       #Walks us through the timestamps list
        while True:
            currentTime = time.time()   #Update the current time for the coming equation
            if(currentTime - startTime >= ts):
                if x == length:
                    playObject = samples[hard].play()
                    playObject.wait_done()
                    x += 1
                    break
                else:
                    rnd = round(((lngth-1)*random.random()))
                    samples[rnd].play()       #Play the given sample out of the file
                    x += 1
                    break
    print("Done playing")

def shuffle_lst(lst):
    length = len(lst)
    rnd = round((length*random.random()))
    rnd2 = round((length*random.random()))
    val = lst[0]
    lst.remove(val)
    lst.reverse()
    val2 = lst[0]
    lst.remove(val2)
    lst.reverse()
    lst.insert(rnd, val)
    lst.insert(rnd2, val2)
    return lst

##--Main--##
def main():
    global bpm, tempo, rhythm, timestamps, plays
    bpm = float(input("What bpm would you like to use? \n>>> "))
    tempo = 60 / bpm
    rhythm = convertToMs(input("What rhythm would you like to play? \n>>> "))
    plays = int(input("How many times would you like the rhythm to be played? \n>>> "))
    timestamps = convertToStamps(rhythm)
    player(timestamps)
main()