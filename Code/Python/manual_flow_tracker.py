import cv2
import matplotlib.pyplot as plt
import numpy as np
import pdb

cap = cv2.VideoCapture(r"E:\WPM\04292024\beet_scan_1.MOV")
i = 0
plt.ion()
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # by default opencv reads images as BGR, here we convert to RGB to be compatible with matplotlib
    plt.imshow(frame)
    plt.show()
    pts = plt.ginput(1)
    plt.close()
    print(pts)