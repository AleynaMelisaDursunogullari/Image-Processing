# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from PIL import Image, UnidentifiedImageError

# Dönüştürülecek dosyaların bulunduğu klasör yolu
klasor_yolu = r"C:\Users\Melisa\Desktop\Yeni klasör (3)"

# Klasördeki tüm dosyaları kontrol et
for dosya_ismi in os.listdir(klasor_yolu):
    # Sadece .jpeg uzantılı dosyaları bul
   # if dosya_ismi.lower().endswith(".jpeg"):
        # Dosya yolunu oluştur
        dosya_yolu = os.path.join(klasor_yolu, dosya_ismi)
        
        try:
            # Resmi aç
            resim = Image.open(dosya_yolu)
            
            # Yeni dosya ismini oluştur (uzantıyı .jpg olarak değiştir)
            yeni_dosya_ismi = dosya_ismi.rsplit(".", 1)[0] + ".jpg"
            yeni_dosya_yolu = os.path.join(klasor_yolu, yeni_dosya_ismi)
            
            # Resmi .jpg formatında kaydet
            resim.convert('RGB').save(yeni_dosya_yolu, 'JPEG')
            
            print(f"Dönüştürüldü: {dosya_yolu} -> {yeni_dosya_yolu}")
            
            # Orijinal .jpeg dosyasını sil
            os.remove(dosya_yolu)
            print(f"Silindi: {dosya_yolu}")
        except UnidentifiedImageError:
            print(f"Resim tanımlanamadı: {dosya_yolu}")
        except Exception as e:
            print(f"Hata oluştu: {dosya_yolu} - {e}")
