__author__ = 'kaustuv'

import serial
import time
f = open("/home/kaustuv/Desktop/text", "r") # change the path here and install pyserial module of python
string = (f.readline()).strip()
arduino1 = serial.Serial(port="/dev/ttyUSB1", baudrate=9600)
for i in string:
        #time.sleep(2)
        print i
        arduino1.write(i)













