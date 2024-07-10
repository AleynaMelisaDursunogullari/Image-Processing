# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:55:34 2024

@author: Melisa
"""

import cv2

# Video dosyasını aç
cap = cv2.VideoCapture(r"C:\Users\Melisa\Desktop\video\WhatsApp Video 2024-06-21 at 22.40.10 (1) (1).mp4")

# Video fps değerini alın
fps = cap.get(cv2.CAP_PROP_FPS)

# 3 saniyede bir kare almak için her 3*fps karede bir kare alınması gerekir
frame_interval = int(fps * 3)

sayac = 10000
frame_count = 0

while True:
    success, img = cap.read()
    
    if not success:
        break
    
    # Yalnızca belirli bir aralıkta bir kare alın
    if frame_count % frame_interval == 0:
        outfile = r'C:\Users\Melisa\Desktop\video\Resimler\resim_%s.jpg' % (sayac)
        sayac += 1
        print(outfile)
        cv2.imwrite(outfile, img)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)  # 1 ms bekleyin (gerekirse ayarlanabilir)
    
    frame_count += 1

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
