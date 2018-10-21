import threading
import simpleaudio as sa
from threading import Thread
import time

samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav"),sa.WaveObject.from_wave_file("./audioFiles/Hard.wav"),sa.WaveObject.from_wave_file("./audioFiles/snare.wav")]
x = 'main'
timestampKick = [0.,1.0]
timestampSnare = [0.5,1.0,1.5]
timestampHat = [0.,0.25,0.5,0.75,1.0,1.25,1.5,1.75]

def func1(s,stamps):
    global timestampKick,timestampSnare,timestampHat, x
    if stamps == 'timestampKick':
        stamps = timestampKick
    elif stamps == 'timestampSnare':
        stamps = timestampSnare
    elif stamps == 'timestampHat':
        stamps = timestampHat
    while True:
        lst = stamps
        if x == 'play' and len(lst) > 0:
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
                            x = 'none'
                            break
                        elif x == 'stop' or x == 'exit()':
                            playObject = samples[s].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            break
                        elif x == 'pause':
                            playObject = samples[s].play()        #Create a playObject so the last sample will be played fully
                            playObject.wait_done()
                            while x == 'pause':
                                time.sleep(0.001)
                            startTime=time.time() - (currentTime - startTime)   #Set the starttime to the new offset
                            break
                        else:
                            samples[s].play()       #Play the given sample out of the file
                            pos += 1
                            break
                if x == 'stop' or x == 'exit()':
                    break
        elif x == 'exit()':
            break
        else:
            x = 'main'
            time.sleep(0.001)

def main():
    global x
    while True:
        if x == 'main':
            x = input(">>> ")
        elif x == 'exit()':
            break

if __name__ == '__main__':
    t1 = Thread(target=main)
    t2 = Thread(target=func1, args=(1,'timestampKick',))
    t3 = Thread(target=func1, args=(2,'timestampSnare',))
    t4 = Thread(target=func1, args=(0,'timestampHat',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

print("Succesfully done program closing")