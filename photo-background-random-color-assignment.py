import cv2
import numpy as np
import random

# Görüntüyü yükleyelim
image_path = r"C:\Users\Melisa\Desktop\4.sinif-tez\Veri-Seti\basparmak-sonuc\benim\validation\thumb\Hand_0000063.jpg"
image = cv2.imread(image_path)

# Görüntü doğrulama
if image is None:
    raise FileNotFoundError(f"Görsel bulunamadı: {image_path}")

# Beyaz arka planı tespit et (beyaz = [255, 255, 255])
# Alt ve üst sınırları beyaz rengi kapsayacak şekilde ayarlıyoruz
lower_white = np.array([200, 200, 200])  # Beyaz için alt sınır
upper_white = np.array([255, 255, 255])  # Beyaz için üst sınır

# Beyaz renk aralığındaki pikselleri tespit et
white_mask = cv2.inRange(image, lower_white, upper_white)

# Rastgele bir renk seçelim (BGR formatında)
random_background_color = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

# Yeni arka planı oluşturma
new_background = np.zeros_like(image)
new_background[:] = random_background_color  # Rastgele renk ile arka plan

# Arka planı değiştiriyoruz
image[white_mask == 255] = new_background[white_mask == 255]

# Çıktıyı kaydedelim
output_image_path = r"C:\Users\Melisa\Desktop\resim_with_random_background4.jpg"
cv2.imwrite(output_image_path, image)

print(f"Yeni arka planlı görüntü kaydedildi: {output_image_path}")
