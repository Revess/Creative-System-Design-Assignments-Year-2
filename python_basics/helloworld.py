#-----Imports------#
import simpleaudio as sa
import threading

#-----Objects------#
name = False

#-----Funtions-----#
def playFile(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def player(numeral):
    x = 0
    if int(numeral) > 20:
        print("This number is too high")
        main()
    else: 
        while x < int(numeral):
            x += 1
            playFile("CowBell.wav")
            print(x)
    if x >= int(numeral):
        print("Thank you for using my program")

#-----Main--------#    
def main():
    global name
    if not name:
        username_obj = input("Please tell us your name: ")
        print("Hello", username_obj)
        name = not name
    num = input("How many times shall I play the sample: ")
    player(num)
main()