# 영상이나 이미지를 회전시켜 띄울 수 있습니다. 90°, 45°, -45° 등 다양한 각도로 회전이 가능합니다.

import cv2

# 원본 이미지로 사용할 src를 선언하고 이미지를 불러옴
src = cv2.imread("Image/ara.jpg", cv2.IMREAD_COLOR)

# 높이, 너비, 채널의 값을 저장
height, width, channel = src.shape

# cv2.getRotationMatrix2D((중심점 X좌표, 중심점 Y좌표), 각도, 스케일)
# matrix에 회전 배열을 생성하여 저장
# 중심점  - Tuple형태로 사용하며 회전할 기준점을 설정
# 각도 -  회전할 각도
# 스케일 - 이미지의 확대 비율 설정
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)

# cv2.warpAffine(원본 이미지, 배열, (결과 이미지 너비, 결과 이미지 높이))
# 결과 이미지로 사용할 dst를 선언하고 회전 함수를 적용
dst = cv2.warpAffine(src, matrix, (width, height))
# 결과 이미지의 너비와 높이로 크기가 선언되며 배열에 따라 이미지가 회전

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# * matrix를 numpy형식으로 선언하여 warpAffine을 적용하여 변환할 수 있습니다.


