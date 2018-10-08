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

##--Functions--##
#Convert a string to a rhythm in miliseconds
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
        shuffle_lst(ms_lst)                         #Mix the old rhythm playlist so we can generate more random lists (See the function for explanation)
    stamps.pop()                                    #Remove the last stamp to so the offset we created at the start (insert a 0) works right
    return stamps

#Play the given list
def player(lst):
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

#Shuffle two items of the given list
def shuffle_lst(lst):
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