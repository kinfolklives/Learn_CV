# 동영상 파일에서 이미지를 얻어와 프레임을 재생

import cv2

# cv2.VideoCapture("경로") : 동영상 파일에서 프레임을 받아옴
capture = cv2.VideoCapture("Image/Star.mp4")

while True:
    # if문을 이용하여 가장 처음 현재 프레임 개수와 총 프레임 개수를 비교
    # capture.get(속성) : capture의 속성을 반환
    # CAP_PROP_POS_FRAMES :현재 프레임 개수
    # cv2.CAP_PROP_FRAME_COUNT : 총 프레임 개수
    
    # 같을 경우, 마지막 프레임이므로, capture.open(경로)를 이용하여 다시 동영상 파일을 불러옴.
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("Image/Star.mp4") 

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0: break # 33ms마다 프레임을 재생

capture.release()
cv2.destroyAllWindows()


# VideoCapture 멤버
# capture.get(속성) : VideoCapture의 속성을 반환합니다.
# capture.grab() : Frame의 호출 성공 유/무를 반환합니다.
# capture.isOpened() : VideoCapture의 성공 유/무를 반환합니다.
# capture.open(카메라 장치 번호 또는 경로) : 카메라나 동영상 파일을 엽니다.
# capture.release() : VideoCapture의 장치를 닫고 메모리를 해제합니다.
# capture.retrieve() : VideoCapture의 프레임과 플래그를 반환합니다.
# capture.set(속성, 값) : VideoCapture의 속성의 값을 설정합니다.

