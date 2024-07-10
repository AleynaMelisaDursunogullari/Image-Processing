import cv2
import os

path = r"C:\Users\Melisa\Desktop\video\WhatsApp Video 2024-06-21"

pre_imgs = os.listdir(path)
print(pre_imgs)
img = []

for i in pre_imgs:
    i = os.path.join(path, i)
    img.append(i)

print(img)

if len(img) == 0:
    raise ValueError("Görüntü dosyaları bulunamadı.")

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
if frame is None:
    raise ValueError(f"Görüntü dosyası okunamadı: {img[0]}")

size = list(frame.shape)
del size[2]
size.reverse()

output_path = r"C:\Users\Melisa\Desktop\uretilen_video.mp4"  # Video dosyasının kaydedileceği yer
video = cv2.VideoWriter(output_path, cv2_fourcc, 30, size)  # output video name, fourcc, fps, size

for i in range(len(img)):
    frame = cv2.imread(img[i])
    if frame is None:
        print(f"Görüntü dosyası okunamadı: {img[i]}")
        continue
    video.write(frame)
    print('frame ', i + 1, ' of ', len(img))

video.release()
print(f'üretilen video {output_path} konumuna kaydedildi.')
