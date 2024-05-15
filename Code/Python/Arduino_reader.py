"""
This script reads the text from an Arduino line-by-line and print in a local file in append ("a") mode. The current time string is prefixed to each line for reference. 

Features to be added: 
- total recording time
- custom output file
- smart warnings 
"""

import serial
import time
import sys

serialCom = serial.Serial("COM4", 9600)


while True:
    s_bytes = serialCom.readline()
    decoded_bytes = s_bytes.decode("utf-8").strip("\r\n")
    print(decoded_bytes)
    with open(r"C:\Users\liuzy\Downloads\rec.txt", "a") as f:
        f.write(time.asctime() + ": " + decoded_bytes + "\n")