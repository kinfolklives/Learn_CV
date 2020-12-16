# 영상이나 이미지의 크기를 원하는 크기로 조절할 수 있습니다.

import cv2


src = cv2.imread("Image/champagne.jpg", cv2.IMREAD_COLOR)

# cv2.resize(원본 이미지, 결과 이미지 크기, 보간법)
# 결과 이미지 크기는 Tuple형을 사용하며, (너비, 높이)를 의미
# 보간법은 이미지의 크기를 변경하는 경우, 변형된 이미지의 픽셀은 추정해서 값을 할당
# 보간법을 이용하여 픽셀들의 값을 할당합니다.
# * 보간법(내삽) : 끝점의 값이 주어졌을 때 그 사이에 위치한 값을 추정하기 위하여 직선 거리에 따라 선형적으로 계산하는 방법
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)

# cv2.resize(원본 이미지, dsize=(0, 0), 가로비, 세로비, 보간법)
# 결과 이미지 크기가 (0, 0)으로 크기를 설정하지 않은 경우, fx와 fy를 이용하여 이미지의 비율을 조절
# fx가 0.3인 경우, 원본 이미지 너비의 0.3배로 변경.
# fy가 0.7인 경우, 원본 이미지 높이의 0.7배로 변경.
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Tip : 결과 이미지 크기와 가로비, 세로비가 모두 설정된 경우, 결과 이미지 크기의 값으로 이미지의 크기가 조절됩니다.

# interpolation 속성
# 속성	의미
# cv2.INTER_NEAREST	이웃 보간법
# cv2.INTER_LINEAR	쌍 선형 보간법
# cv2.INTER_LINEAR_EXACT	비트 쌍 선형 보간법
# cv2.INTER_CUBIC	바이큐빅 보간법
# cv2.INTER_AREA	영역 보간법
# cv2.INTER_LANCZOS4	Lanczos 보간법
# https://076923.github.io/posts/Python-opencv-8/