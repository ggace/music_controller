import make_wav
import keyboard
import play_wav
import os
import threading
freq = 400
i = 0
playing = False
def make_sound():
    global freq
    global i
    global playing
    make_wav.make_sound(freq, i)
    
    while not(keyboard.is_pressed('escape')):
        if(keyboard.is_pressed('w')):
            i += 1
            freq += 10
            make_wav.make_sound(freq, i)
        elif(keyboard.is_pressed('s')):
            i += 1
            freq -= 10
            make_wav.make_sound(freq, i)
        if playing:
            play_wav.stop(i)
            playing = False

def play():
    global i
    
    play_wav.play(i)
    playing = True
    
        

threading.Thread(target = make_sound).start()
threading.Thread(target = play).start()
