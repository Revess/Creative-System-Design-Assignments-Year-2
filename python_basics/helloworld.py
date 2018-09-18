#-----Imports------#
import simpleaudio as sa
import threading

#-----Funtions-----#
def playFile(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def player(numeral):
    x = 0
    while x < int(numeral):
        x += 1
        playFile("CowBell.wav")
        print(x)
    if x >= int(numeral):
        print("Thank you for using my program")

#-----Main--------#
username_obj = input("Please tell us your name: ")
print("Hello", username_obj)
num = input("How many times play the sample: ")
player(num)