#----Imports----#
import simpleaudio as sa
import time

#----Objects----#
#Machine on or off
running = True
#State of machine
state = 'main'
#Path to file
filePath = "CowBell.wav"
#Bpm in ms
bpm = 0.5
#Amount of playtimes
numOfPlays = 1
#List that contains the rhythm
rhythm_lst = [1, 1, 1, 1,]
#List of milisecond rhythms
ms_lst = [0.5, 0.5, 0.5, 0.5]
#Possible rhythms
rhythm_obj_lst = [1, 2, 4, 8, 16, 32]

#----Functions----#
def playFile():
    wave_obj = sa.WaveObject.from_wave_file(filePath)
    wave_obj.play()

def play():
    x = 0
    while x < numOfPlays:
        for i in ms_lst:
            playFile()
            time.sleep(i)
        x += 1
    if x >= numOfPlays:
        print("Sequence completed")
        return

#----Main----#
#Setup#
print("Welcome to the beatmachine. Type help for any instructions. \n'>>>' will indicate you are in a command and '>>' shows you are back in the main menu. \nFrom here you can execute commands")

#Loop#
while running:
####Setup####
    if state == 'main':
        state = input(">> ")

####Fundamentals####
#---Help
    elif state == 'help':
        print("The following commands can be used: \ncurrentFile   play \nexit()        rhythm \ngetFile       tempo \nhelp          testFile \nnumOfPlays    testSequencer")
        state = 'main'

####Commands####
##----currentFile----##
    elif state == 'currentFile':
        print(filePath)
        state = 'main'
##----play----##
    elif state == 'play':
        play()
        state = 'main'
##----rhythm----##
    elif state == 'rhythm':
        print("Would you like to view or create the rhythm?")
        state = input(">>> ")
        if state == 'view':
            print("The current rhythmSequence is: " + str(rhythm_lst))
            state = 'main'
        elif state == 'create':
            print("Give your desired rhythm: ")
            rhythm_lst = []
            ms_lst = []
            rhythm_lst = input(">>> ")
            str_lst = rhythm_lst.split()
            for i in str_lst:
                if i == '|':
                    str_lst.remove(i)
            float_lst = [float(i) for i in str_lst]
            for i in float_lst:
                for x in rhythm_obj_lst:
                    if i == x:
                        i = i/4
                        i = bpm/i
                        ms_lst.append(i)
            state = 'main'
        else:
            state = 'main'
##----getFile----##
    elif state == 'getFile':
        filePath = input(">>> ")
        state = 'main'
##----tempo----##
    elif state == 'tempo':
        print("Would you like to view or set the tempo?")
        state = input(">>> ")
        if state == 'view':
            print("The current tempo is set to " + str(60/bpm) + " BPM")
            state = 'main'
        elif state == 'set':
            print("Give your desired tempo in BPM:")
            bpm = float(input(">>> "))
            print("The current tempo has been set to " + str(bpm) + " BPM")
            bpm = 60/bpm
            state = 'main'
##----testFile----##
    elif state == 'testFile':
        print("Starting file")
        playFile()
        print("Done playing")
        state = 'main'
##----numOfPlays----##
    elif state == 'numOfPlays':
        numOfPlays = int(input(">>> "))
        if numOfPlays > 20:
            print("This number is too high")
        else:
            state = 'main'
#---Exit message to exit program
    elif state == 'exit()':
        exit()
#---Invalid input
    else:
        print("Unkown command, to see the full list of commands use help")
        state = 'main'