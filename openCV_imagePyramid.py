# 이미지 피라미드 (Image Pyramid)란 이미지의 크기를 변화시켜 원하는 단계까지 샘플링하는 작업입니다.
# >>> 영상이나 이미지를 확대, 축소시켜 띄울 수 있습니다.

import cv2

src = cv2.imread("Image/fruits.jpg", cv2.IMREAD_COLOR)

# 해당 이미지의 높이, 너비, 채널의 값을 저장
height, width, channel = src.shape


# 너비와 높이를 이용하여 dstsize (결과 이미지 크기)을 설정
dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT);
# cv2.pyrUp(원본 이미지, 결과 이미지 크기, 픽셀 외삽법)
# cv2.pyrUp(원본 이미지) : 이미지를 2배로 확대
# pyrUp() >>  결과 이미지가 이미지 크기의 2배
# 픽셀 외삽법은 이미지를 확대 또는 축소할 경우, 영역 밖의 픽셀은 추정해서 값을 할당.
# 이미지 밖의 픽셀을 외삽하는데 사용되는 "테두리 모드" 입니다. (외삽 방식을 설정)

# cv2.pyrDown(원본 이미지)로 이미지를 1/2배로 축소
# cv2.pyrUp() 함수와 동일한 매개변수를
# 결과 이미지 크기는 (width/2, height/2)를 사용
dst2 = cv2.pyrDown(src);

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# pyrUp()과 pyrDown() 함수에서 결과 이미지 크기와 픽셀 외삽법은 기본값으로 설정된 인수를 할당해야하므로 생략하여 사용합니다.
# 피라미드 함수에서 픽셀 외삽법은 cv2.BORDER_DEFAULT만 사용할 수 있습니다.
# 이미지를 1/8배, 1/4배 ,4배, 8배 등의 배율을 사용해야하는 경우, 반복문을 이용하여 적용할 수 있습니다.


