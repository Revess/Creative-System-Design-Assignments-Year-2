##--Imports--##
import simpleaudio as sa
import time

##--Objects--##
samples = [sa.WaveObject.from_wave_file("./audioFiles/CowBell.wav"),sa.WaveObject.from_wave_file("./audioFiles/snare.wav"),sa.WaveObject.from_wave_file("./audioFiles/SecretKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/RoninKick.wav"),sa.WaveObject.from_wave_file("./audioFiles/PrydaSnare.wav"),sa.WaveObject.from_wave_file("./audioFiles/Hard.wav")]
bpm = 120
tempo = 60 / bpm
timestamps = [0]
rhythm = []
rhythm_obj_lst = [1, 2, 4 ,8 ,16]
timestamps = []
plays = 0
measure = []

##--Main--##
def main():
    global bpm, plays, rhythm_obj_lst, measure
    state = ['main']
    length = 0
    print("Welcome to the irregular beat generator. Type help to display all the options")
    while True:
        if state[0] == 'main':
            state = input('>>> ').lower().split()
            length = len(state)
        elif state[0] == 'bpm':
            while True:
                if length == 1:
                    state = [input('What BPM would you like to use? \n>>> ').lower()]
                    state = state[0].split()
                    statelength = len(state)
                    if statelength > 1:
                        print("Too many arguments given")
                    if statelength < 1:
                        print("Not enough arguments given")
                    elif not state[0].isdigit:
                        print('Invalid argument')
                    elif int(state[1]) > 0 and int(state[1]) < 999:
                        bpm = state[1]
                        break
                elif length == 2:
                    break
                elif state == 'back':
                    break
                else:
                    print('Invalid argument for command" "bpm')
            state = ['main']
        elif state[0] == 'loop':
            succes = False
            while True:
                if length == 1:
                    while True:
                        state = [input('How many bars should the rhythm be? \n>>> '.lower())]
                        state = state[0].split()
                        statelength = len(state)
                        if state[0] == 'back':
                            break
                        elif statelength > 1:
                            print("Too many arguments given")
                        elif statelength < 1:
                            print("Not enough arguments given")
                        elif not state[0].isdigit():
                            print('Invalid argument')
                        elif int(state[0]) > 0 and int(state[0]) < 20:
                            plays = state[0]
                            succes = True
                            break
                        else:
                            print('Invalid argument')
                elif length == 2:
                    if state[1] == 'length':
                        while True:
                            state = [input('How many bars should the rhythm be? \n>>> '.lower())]
                            if state[0] == 'back':
                                break
                            elif not state[0].isdigit():
                                print('Invalid argument')
                            elif int(state[0]) > 0 and int(state[0]) < 20:
                                plays = state[0]
                                succes = True
                                break
                            else:
                                print('Invalid argment')
                elif state == 'back':
                    break
                if not succes:
                    if not state[0] == 'back':
                        if length == 3:
                            if not state[2].isdigit() or not state[1] == 'length':
                                print('Invalid argument(s) for command: "loop"')
                                break
                            elif int(state[2]) > 0 and int(state[2]) < 20:
                                plays = state[2]
                                succes = True
                        else:
                            print('Invalid argument for command: "loop"')
                            break
                    else:
                        break
                else:
                    print('The number of loops has been set to: ' + str(plays))
                    break
            state = ['main']
        elif state[0] == 'measure':
            succes = False
            while True:
                if length == 1:
                    while True:
                        state = [input('In what measure whould I play the rhythm? \n>>> ').lower()]
                        state = state[0].split('/')
                        statelength = len(state)
                        if state[0] == 'back':
                            break
                        elif statelength <= 1:
                            print("Not enough arguments given")
                        elif statelength > 2:
                            print("Too many arguments given")
                        elif not state[0].isdigit or not state[1].isdigit:
                            print('Invalid argument')
                        elif int(state[0]) < 20:
                            for x in rhythm_obj_lst:
                                if x == int(state[1]):
                                    measure = state.copy()
                            if len(measure) > 0:
                                succes = True
                                break
                            else:
                                print("Invalid measure argument")
                elif length == 2:
                    while True:
                        state = state [1].split('/')
                        statelength = len(state)
                        if state[0] == 'back':
                            break
                        elif statelength <= 1:
                            print("Not enough arguments given")
                        elif statelength > 2:
                            print("Too many arguments given")
                        elif not state[0].isdigit or not state[1].isdigit:
                            print('Invalid argument')
                        elif int(state[0]) < 20:
                            for x in rhythm_obj_lst:
                                if x == int(state[1]):
                                    measure = state.copy()
                            if len(measure) > 0:
                                succes = True
                                break
                            else:
                                print("Invalid measure argument")
                elif state == 'back':
                    break
                if not succes:
                    if not state[0] == 'back':

                            print('Invalid argument for command: "measure"')
                            break
                    else:
                        break
                else:
                    print('The measure has been set to: ' + str(measure[0]) + "/" + str(measure[1]))
                    state = ['main']
                    break
        else:
            print('Unkown command, type "help" to see the full list of commands')
            state = ['main']
main()

##Helpfile: None of the arguments or the commands are case sensitive. 
# If only command is typen the user will be asked for arguments
# -Loop, uses argument length, length needs a number. Example: Loop length 10
# -Measure, uses argument "measure type". Example: Measure 4/4
# -BPM, uses argument "tempo number". Example: BPM 120
