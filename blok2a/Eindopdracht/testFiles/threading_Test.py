import threading
import simpleaudio as sa
from threading import Thread
import time

samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav"),sa.WaveObject.from_wave_file("./audioFiles/Hard.wav"),sa.WaveObject.from_wave_file("./audioFiles/snare.wav")]
x = 'main'

def func1(t,s):
    global x
    tick = 0
    while True:
        if x == 'exit()':
            break
        else:
            time.sleep(t)
            samples[s].play()
            tick += 1

def main():
    global x
    while True:
        if x == 'main':
            x = input(">>> ")
        elif x == 'exit()':
            break

if __name__ == '__main__':
    t1 = Thread(target=main)
    t2 = Thread(target=func1, args=(1,0,))
    t3 = Thread(target=func1, args=(2,1,))
    t4 = Thread(target=func1, args=(1.5,2,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

print("Succesfully done program closing")