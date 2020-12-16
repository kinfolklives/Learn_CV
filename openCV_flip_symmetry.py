# 영상이나 이미지를 대칭시켜 띄울 수 있습니다. 상하 또는 좌우방향으로 대칭할 수 있습니다.

import cv2

# src 선언, 이미지를 불러움.
src = cv2.imread("Image/glass.jpg", cv2.IMREAD_COLOR) 

# cv2.flip(원본 이미지, 대칭 방법) - 대칭방법: 0 or 1
# 0: 상하, 1: 좌우 
# 결과 이미지로 사용할 dst를 선언하고 대칭 함수를 적용
dst = cv2.flip(src, 0)                                

# 이미지를 출력
cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 대칭 방법 중 상수를 0보다 낮은 값을 입력할 경우, 상하 대칭으로 간주합니다.
# 대칭 방법 중 상수를 1보다 높은 값을 입력할 경우, 좌우 대칭으로 간주합니다.

