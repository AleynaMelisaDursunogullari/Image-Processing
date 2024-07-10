# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

cap=cv2.VideoCapture(r"C:\Users\Melisa\Desktop\video\WhatsApp Video 2024-06-21 at 22.40.10 (1) (1).mp4")

sayac=10000

while True:
    success, img=cap.read()
    outfile =r'C:\Users\Melisa\Desktop\video\Resimler\resim_%s.jpg' % (sayac)
    sayac+=1
    print(outfile)
    cv2.imwrite(outfile, img)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    