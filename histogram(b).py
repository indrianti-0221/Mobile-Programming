import cv2
import numpy as np

# Baca gambar
image = cv2.imread('gray.jpg')

# Konversi gambar ke grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tentukan nilai peningkatan kecerahan
brightness_factor = 78  # Ubah nilai ini sesuai kebutuhan Anda

# Tambahkan nilai peningkatan kecerahan ke setiap piksel dalam gambar grayscale
brightened_image = np.clip(grayscale_image.astype(int) + brightness_factor, 0, 255).astype(np.uint8)

# Menampilkan gambar yang telah ditingkatkan kecerahannya
cv2.imshow('Brightened Grayscale Image', brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
