#-----Imports------#
import simpleaudio as sa
import time

#-----Objects------#
name = False
rhythm_obj_lst = [0.25, 0.375, 0.5, 0.75, 1, 1.5, 2, 3, 4, 6]

#-----Funtions-----#
def playFile(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    wave_obj.play()

def player(numeral, rhythm):
    x = 0
#---Check if the asked amount of plays is not too high (just for safety reasons)
    if int(numeral) > 20:
        print("This number is too high")
        main()
    else: 
#-------While loop that counts down the number of plays
        while x < int(numeral):
#-----------Checks every ms value to create the rhythm
            for i in rhythm:
                playFile("CowBell.wav")
                time.sleep(i)
            x += 1
            print(x)
#---Ends program
    if x >= int(numeral):
        print("Thank you for using my program")
        exit()

#Function to convert rhythmic values to miliseconds
def beatToMS(val, tempo):
#---Check the values in the rhythm rules list check if the value is correct
    for x in rhythm_obj_lst:
        if x == val:
#-----------Transfor the rhythm input to ms
            return val*tempo
    else:
#-------The given rhythm has an unkown value, shows which value and returns to the main to ask the user to try again
        print("This is not a rhythmic value: " + str(val))
        main()

def filtering(lst):
    for i in lst:
        if i == "|":
            lst.remove('|')
    return lst

#Setup the conversionstructure to convert the list.
def convertList(lst, tempo):
#---Convert the input string to a list
    str_lst = lst.split()
#---Filter out the dashes
    str_lst = filtering(str_lst)
#---Convert the list types to floats
    float_lst = [float(i) for i in str_lst]
#---seconds per beat
    spb = 60000./float(tempo)/1000.
#---Sort the list into the different ms
    ms_lst = [beatToMS(i, spb) for i in float_lst]
    return ms_lst

#-----Main--------#    
def main():
    global name
#---Ask once for name
    if not name:
        username_obj = input("Please tell us your name: ")
        print("Hello", username_obj)
        name = not name
#---Ask for the BPM
    bpm = input("What bpm would you like to use: ")
#---Ask for the wanted rhythm
    rhythm = input("Give your rhythm in decimal values (in bits): ")
#---Ask how many times to play the rhythm
    num = input("How many times shall I play the rhythm: ")
#---Create a list of the given rhythm in ms
    rhythm_lst = convertList(rhythm, bpm)
#---Play the given rhythm for the user
    player(num, rhythm_lst)
main()