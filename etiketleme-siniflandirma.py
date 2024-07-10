# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:22:53 2024

@author: Melisa
"""

import os
from ultralytics import YOLO
import cv2

# Modelin yolu
model_path = r"C:\Users\Melisa\Desktop\best(2).pt"
# Fotoğrafların bulunduğu klasör
image_folder = r"C:\Users\Melisa\Desktop\Yeni klasör (4)"
# Txt dosyalarının kaydedileceği klasör
output_folder = os.path.join(image_folder, "labels")
# Etiketlenmiş görüntülerin kaydedileceği klasör
output_image_folder = os.path.join(image_folder, "labeled_images")

# Txt dosyalarının kaydedileceği klasörü oluştur
os.makedirs(output_folder, exist_ok=True)
# Etiketlenmiş görüntülerin kaydedileceği klasörü oluştur
os.makedirs(output_image_folder, exist_ok=True)

# Modeli yükle
model = YOLO(model_path)

def convert_to_yolo_format(x, y, w, h, img_width, img_height):
    x_center = (x + w / 2) / img_width
    y_center = (y + h / 2) / img_height
    width = w / img_width
    height = h / img_height
    return x_center, y_center, width, height

# Tüm görüntüleri işle
for image_name in os.listdir(image_folder):
    if image_name.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_folder, image_name)
        img = cv2.imread(image_path)
        img_height, img_width = img.shape[:2]
        
        results = model(image_path)

        label_file_path = os.path.join(output_folder, os.path.splitext(image_name)[0] + ".txt")

        with open(label_file_path, 'w') as f:
            if len(results[0].boxes) > 0:
                for box in results[0].boxes:
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    w = x2 - x1
                    h = y2 - y1
                    x_center, y_center, width, height = convert_to_yolo_format(x1, y1, w, h, img_width, img_height)
                    
                    class_name = results[0].names[int(box.cls)]
                    label = 1 if class_name == "chickpeas" else 0
                    f.write(f"{label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

                    # Görüntüye dikdörtgen çizin ve etiket ekleyin
                    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 3)
                    cv2.putText(img, str(label), (max(0, int(x1)), max(35, int(y1))), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            else:
                f.write("0\n")
        
        # Etiketlenmiş görüntüyü kaydedin
        output_image_path = os.path.join(output_image_folder, image_name)
        cv2.imwrite(output_image_path, img)

cv2.destroyAllWindows()
