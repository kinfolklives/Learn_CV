# 영상이나 이미지의 크기를 원하는 크기로 조절할 수 있습니다.

import cv2

src = cv2.imread("Image/pawns.jpg", cv2.IMREAD_COLOR)

dst = src.copy() 
dst = src[100:600, 200:700]

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

