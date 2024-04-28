import cv2

# Baca gambar
image = cv2.imread('albert.jpg')

# Lakukan flipping horizontal
flipped_horizontal = cv2.flip(image, 1)

# Lakukan flipping vertikal
flipped_vertical = cv2.flip(image, 0)

# Tampilkan gambar asli dan gambar yang telah di-flipping
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Horizontal', flipped_horizontal)
cv2.imshow('Flipped Vertical', flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
