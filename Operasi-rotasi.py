import cv2

# Baca gambar
image = cv2.imread('albert.jpg')

# Tentukan sudut rotasi (dalam derajat)
angle = 45  # Ubah nilai ini sesuai kebutuhan Anda

# Dapatkan tinggi dan lebar gambar
height, width = image.shape[:2]

# Hitung titik tengah gambar
center = (width // 2, height // 2)

# Lakukan rotasi gambar
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Tampilkan gambar asli dan gambar yang telah dirotasi
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
