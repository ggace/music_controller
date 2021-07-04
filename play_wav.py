import winsound
import time
from playsound import playsound
import threading

def play(i):
    
    playsound(f'audio/test{i}.wav')
def stop(i):
    
    winsound.PlaySound(f'audio\\test{i}.wav', winsound.SND_ASYNC)


