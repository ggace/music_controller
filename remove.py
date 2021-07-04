from os import listdir
from os.path import isfile, join
import os
onlyfiles = [f for f in listdir('audio') if isfile(join('audio', f))]

while(True):
    onlyfiles = [f for f in listdir('audio') if isfile(join('audio', f))]
    if(len(onlyfiles) > 1):
        for i in range(len(onlyfiles)-1):
            os.remove('audio/' + onlyfiles[i])