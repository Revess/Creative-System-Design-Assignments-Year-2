##--Imports--##
import simpleaudio as sa
import time
import random
import threading
from threading import Thread

##--Objects--##
samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav"),sa.WaveObject.from_wave_file("./audioFiles/snare.wav"),sa.WaveObject.from_wave_file("./audioFiles/SecretKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/RoninKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/PrydaSnare.wav"),sa.WaveObject.from_wave_file("./audioFiles/Hard.wav")]
bpm = 120
hard = 5
tempo = 60 / bpm
timestamps = [0]
rhythm = []
rhythm_obj_lst = [1, 2, 4 ,8 ,16]
timestamps = []
running = False
setup = False
playing = 0                                     #0 = Stop, 1 = Play, 2 = Pause, (When I get to it maybe even 3 = Reverse)

##--Functions--##
#Shuffle the list
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
def convertToStamps():
    global running, timestamps, rhythm, setup, playing
    x = 0
    t = 0
    nrhythm = rhythm
    while running:
        if setup:
            for f in rhythm:
                x += f
                timestamps.append(x)
            setup = False
            shuffle_lst(nrhythm)
        elif playing == 1:
            t = 0
            for f in nrhythm:
                x += f
                timestamps.append(x)
            shuffle_lst(nrhythm)
        elif playing == 2:
            if t <= len(rhythm):
                for f in rhythm:
                    x += f
                    timestamps.append(x)
                    t+=1
            shuffle_lst(rhythm)
        elif playing == 3:
            setup = True
            playing = 0

#Play rhythm
def player():
    global running, timestamps, playing
    while running:
        if playing == 1:
            startTime = time.time()
            ts = timestamps.pop(0)
            while True:
                currentTime = time.time()
                if(currentTime - startTime >= ts):
                    # rnd = round(((lngth-1)*random.random()))
                    samples[hard].play()
                    if timestamps:
                        ts = timestamps.pop(0)
                        playing = 0
                elif playing == 2:
                    if(currentTime - startTime >= ts):
                        playObject = samples[hard].play()
                        playObject.wait_done()
                    break
                elif playing == 3:
                    if(currentTime - startTime >= ts):
                        playObject = samples[hard].play()
                        playObject.wait_done()
                    timestamps = [0]
                    break
                else:
                    time.sleep(0.001)

def stater():
    global bpm, rhythm, playing, running
    state = 'main'
    command = ""
    while running:
        if state == 'main':
            command = input(">>> ")
            command.split()
            print(command)
        if command[0] == 'play()':
            playing = 1
            print(playing)
        if command[0] == 'stop()':
            playing = 3
            print(playing)
        if command[0] == 'pause()':
            playing = 2
            print(playing)
        if command[0] == 'bpm:' or 'bpm':
            bpm = command[5]
            print(bpm)
        if command[0] == 'exit()':
            running = False
            print(running)


##--Main--##
def main():
    global bpm, tempo, rhythm, setup, running
    bpm = float(input("It is time to setup the program: \nWhat bpm would you like to use? \n>>> "))
    tempo = 60 / bpm
    rhythm = convertToMs(input("What rhythm would you like to play? \n>>> "))
    setup = True
    running = True

    run_event = threading.Event()
    run_event.set()
    t1 = threading.Thread(target = convertToStamps)
    t2 = threading.Thread(target = player)
    t3 = threading.Thread(target = stater)

    t1.start()
    t2.start()
    t3.start()

    try:
        while 1:
            time.sleep(0.001)
    except (KeyboardInterrupt, running == False):
        print("Attempting to close thread, please wait...")
        run_event.clear()
        t1.join()
        t2.join()
        t3.join()
        print("All threads are successfully closed")
        print("All threads are successfully closed")

if __name__ == '__main__':
    main()