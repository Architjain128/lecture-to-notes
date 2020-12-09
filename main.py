#  error handling remaining

import os
import sys
import speech_recognition as sr

delete = False
filer=input("Enter video : ")
filename, file_extension = os.path.splitext(filer)
filename
filert = filename + '.wav'

if(filer != filert):
    command = "ffmpeg -i "+filer+" "+filert
    os.system(command)
    delete = True

textx=filename+'.txt'
r=sr.Recognizer()
audio = sr.AudioFile(filert)

with audio as source:
    audio = r.record(source)
    with open(textx, 'w') as f:
        print(r.recognize_google(audio), file=f)

if(delete == True):
    os.remove(filert)