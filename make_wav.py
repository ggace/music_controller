from IPython.display import Audio, display
import numpy as np

import soundfile as sf


def single_tone(frequecy, sampling_rate=44100, duration=1):
    # frequency: 주파수
    # sampling_rate: 초당 샘플링 데이터 수. 디폴트 44100
    # duration: 지속 시간. 단위 초. 디폴트 1초
    t = np.linspace(0, duration, int(sampling_rate))
    y = np.sin(2 * np.pi * frequecy * t)
    return y


def make_sound(freq, i):

    
    rate = 44100
    during = 1
    
    
    sf.write(f'audio/test{i}.wav', single_tone(freq, rate * during, during), 44100)
