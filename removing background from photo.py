from rembg import remove

# Giriş ve çıkış dosyalarının yollarını belirtelim
input_path = r"C:\User\\20241202_145916.jpg"
output_path = r"C:\Users\Desktop\foto.jpg"

# Görüntüyü okuma ve işleme
with open(input_path, 'rb') as i_:
    with open(output_path, 'wb') as o_:  # 'wb' yazım hatası düzeltildi
        output = remove(i_.read())  # 'remove' fonksiyonu ile arka plan kaldırma
        o_.write(output)  # İşlenen resmi çıkış dosyasına yazma

print(f"İşlenmiş görüntü başarıyla kaydedildi: {output_path}")
