#-----Imports------#
import simpleaudio as sa
import time

#-----Objects------#
name = False

#-----Funtions-----#
def playFile(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def player(numeral, rhythm):
    x = 0
    if int(numeral) > 20:
        print("This number is too high")
        main()
    else: 
        while x < int(numeral):
            for i in rhythm:
                playFile("CowBell.wav")
                time.sleep(i)
            x += 1
            print(x)
    if x >= int(numeral):
        print("Thank you for using my program")

def beatToMS(val, tempo):
    if val == 4:
        return tempo*val
    if val == 2:
        return tempo*val
    if val == 1:
        return tempo*val 
    if val == 0.5:
        return tempo*val
    if val == 0.25:
        return tempo*val
    if val == 0.125:
        return tempo*val


def convertList(lst, tempo):
    str_lst = lst.split()
    float_lst = [float(i) for i in str_lst]
    #seconds per beat
    spb = 60000./float(tempo)/1000.
    #Sort the list into the different ms
    ms_lst = [beatToMS(i, spb) for i in float_lst]
    return ms_lst

#-----Main--------#    
def main():
    global name
    #Ask once for name
    if not name:
        username_obj = input("Please tell us your name: ")
        print("Hello", username_obj)
        name = not name
    #Ask for the BPM
    bpm = input("What bpm would you like to use: ")
    #Ask for the wanted rhythm
    rhythm = input("Give your rhythm in decimal values (in bits): ")
    #Ask how many times to play the rhythm
    num = input("How many times shall I play the rhythm: ")
    rhythm_lst = convertList(rhythm, bpm)
    player(num, rhythm_lst)
main()