import cv2

# Baca gambar
image = cv2.imread('albert.jpg')

# Tentukan nilai peningkatan kecerahan
brightness_factor = 100  # Ubah nilai ini sesuai kebutuhan Anda

# Tambahkan nilai peningkatan kecerahan ke setiap saluran warna dalam gambar
brightened_image = cv2.add(image, brightness_factor)

# Menampilkan gambar yang telah ditingkatkan kecerahannya
cv2.imshow('Brightened Image', brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
