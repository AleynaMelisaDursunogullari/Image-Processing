# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 16:58:32 2024

@author: Melisa
"""

import os
import shutil

# İşlem yapılacak klasör yolu
klasor_yolu = r"C:\Users\Desktop\Yeni klasör (3)"

# Klasördeki tüm dosyaları listele
dosya_listesi = os.listdir(klasor_yolu)

# Yeniden isimlendirme işlemi için sayaç
sayac = 943

# Dosya listesini sıralı olarak işle
for dosya_ismi in sorted(dosya_listesi):
    # Sadece .jpg uzantılı dosyaları işle
    # if dosya_ismi.lower().endswith(".jpg"):
    # Yeni dosya ismini oluştur
    yeni_dosya_ismi = f"image{sayac}.jpg"
    eski_dosya_yolu = os.path.join(klasor_yolu, dosya_ismi)
    yeni_dosya_yolu = os.path.join(klasor_yolu, yeni_dosya_ismi)
    
    # Dosyayı yeni isimle taşı
    shutil.move(eski_dosya_yolu, yeni_dosya_yolu)
    
    print(f"Yeniden isimlendirildi: {eski_dosya_yolu} -> {yeni_dosya_yolu}")
    
    # Sayacı bir artır
    sayac += 1
