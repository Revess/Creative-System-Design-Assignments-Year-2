from pynput.keyboard import Key,Listener,Controller
from threading import Thread
import time

statedepth = -1
statestorage = []
keyboard = Controller()
command = ''
s = "FUCK"

def on_press(key):
    pass

def on_release(key):
    global statedepth, statestorage, command
    if key == Key.up:
        if len(statestorage) == 0:
            keyboard.type('')
        elif statedepth >= len(statestorage)-1:
            for stor in list(statestorage[statedepth]):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            for stor in list(statestorage[statedepth]):
                keyboard.type(str(stor))
        else:
            statedepth+=1
            for stor in list(statestorage[statedepth-1]):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            for stor in list(statestorage[statedepth]):
                keyboard.type(str(stor))
    elif key == Key.down:
        if statedepth <= 0:
            if statedepth >-1:
                statedepth = -1
            keyboard.type('')
        else:
            statedepth-=1
            for stor in list(statestorage[statedepth]):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
            for stor in list(statestorage[statedepth]):
                keyboard.type(str(stor))
    elif command == 'exit()':
        return False

def main():
    global state, statedepth,statestorage,command
    state = ['main']
    while True:
        if state[0] == 'main':
            statedepth = -1
            state = input(">>> ").lower().split()
            if not len(state) == 0:
                string = ' '.join(state)
                statestorage.insert(0,string)
            else:
                state = ['main']
        elif state[0] == 'exit()':
            command = 'exit()'
            break
        else:
            state = ['main']

if __name__ == '__main__':
    t1 = Thread(target=main)

    t1.start()
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

    t1.join()