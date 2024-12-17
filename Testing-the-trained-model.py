# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:16:54 2024

@author: Melisa
"""

import cv2
from ultralytics import YOLO
import cvzone

# Modeli yükleyin
model = YOLO(r"C:\train\weights\best.pt")

# Görüntüyü yükleyin (Video yerine resim kullanıyoruz)
image_path = r"C:\Users\images.jpg"
img = cv2.imread(image_path)

# Görüntünün yüklendiğinden emin olun
if img is None:
    print("Error: Image not found.")
else:
    # Orijinal boyutları al
    original_height, original_width = img.shape[:2]
    
    # Yeni boyutları hesapla (orijinal boyutların 1/4'ü)
    new_width = original_width // 6
    new_height = original_height // 6

    # Görüntüyü yeniden boyutlandır
    img = cv2.resize(img, (new_width, new_height))
    
    # YOLO modeline gönder ve sonuçları al
    results = model(img, stream=True)

    try:
        for r in results:
            boxes = r.boxes
            names = r.names

            for box in boxes:
                # Nesne sınıfı adını al
                variable = names[int(box.cls)]
                
                # Confidence değerini al
                confidence = box.conf[0]  # Confidence değeri
                
                # Koordinatları al
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Nesne etrafına dikdörtgen çizme
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                
                # Confidence değerini yuvarla ve metinle birleştir
                text = f"{variable} {confidence:.2f}"  # Örnek: "domates 0.85"
                
                # Metni görüntüye yazdır
                cvzone.putTextRect(img, text, (max(0, x1), max(35, y1)), scale=2,thickness=2)

        # İşlenmiş görüntüyü göster
        cv2.imshow('img', img)
        cv2.waitKey(0)  # Görüntü ekranda kalacak
        cv2.destroyAllWindows()

        # Sonuçları kaydet
        output_image_path = r"C:\Users\image.jpg"
        success = cv2.imwrite(output_image_path, img)
        if success:
            print(f"Output image saved at: {output_image_path}")
        else:
            print("Error: Failed to save the output image.")

    except cv2.error as e:
        print(f"An error occurred: {e}")
