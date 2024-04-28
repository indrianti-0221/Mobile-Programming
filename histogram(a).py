import cv2

# Baca gambar
image = cv2.imread('citra.jpg')

# Ubah warna gambar menjadi grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tampilkan gambar asli dan gambar hasil konversi
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('gambar_grayscale.jpg', grayscale_image)
