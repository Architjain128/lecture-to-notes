import cv2
import os
import sys

filer=input("Enter video : ")
filename, file_extension = os.path.splitext(filer)
filename
filert = filename + '.mp4'

if(filer != filert):
    command = "ffmpeg -i "+filer+" "+filert
    os.system(command)

vidcap = cv2.VideoCapture(filert)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./img/"+filename+"frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1