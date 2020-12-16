import cv2

image = cv2.imread("Image/lunar.jpg", cv2.IMREAD_ANYCOLOR)

# image = cv2.imread("경로", mode) > 이미지를 불러와 변수에 저장
# mode 
# cv2.IMREAD_UNCHANGED : 원본 사용
# cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
# cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
# cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
# cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
# cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
# cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
# cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
# cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
# cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
# cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용

cv2.imshow("Moon", image)

height, width, channel = image.shape  # 해당 이미지의 높이, 너비, 채널의 값을 확인
print(height, width , channel)

# Tip : 유효 비트가 많을 수록 더 정밀해집니다.
# Tip : 채널이 3일 경우, 다색 이미지입니다. 채널이 1일 경우, 단색 이미지입니다.


# cv2.waitkey(time): time마다 키 입력상태를 받아옴. 0일 경우, 지속적으로 검사하여 해당 구문을 넘어가지 않습니다.
cv2.waitKey(0) 
cv2.destroyAllWindows()






