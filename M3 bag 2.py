# import library open cv
import cv2

#load image (simpan image dalam 1 folder dengan source code)
img = cv2.imread('Politeknik-TEDC-Bandung.png',0)
#tampilkan dalam satu windows utama
cv2.imshow('Politeknik-TEDC-Bandung', img)
#tunggu action dari user
cv2.waitKey(0)
#hapus semua windows (form) yang ada
cv2.destroyAllWindows()