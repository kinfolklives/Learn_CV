import cv2

# cv2.VideoCapture(n) / n : 카메라의 장치 번호 (내장 0, 외장 1~n)  
capture = cv2.VideoCapture(0) 

# capture.set(option, n) : 프레임 너비, 높이 등등 옵션 넣을 수 있음, n : 값
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# while문으로 영상 출력 반복
# capture.read() : 카메라 상태와 프레임 받아옴
# ret: 카메라 상태가 저장, 정상 > True 반환 
# frame: 현재 프레임이 저장
# cv2.imshow("윈도우 창 제목", 이미지) : 윈도우 창에 이미지 보여주기

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) > 0: break

# if문을 이용하여 키 입력이 있을 때 까지 while문을 반복합니다.
# cv2.waitkey(time)이며 time마다 키 입력상태를 받아옵니다.
# 키가 입력될 경우, 해당 키의 아스키 값을 반환합니다.
# 즉, 어떤 키라도 누를 경우, break하여 while문을 종료합니다.
# Tip : time이 0일 경우, 지속적으로 검사하여 프레임이 넘어가지 않습니다.
# Tip : if cv2.waitKey(1) == ord('q'): break으로 사용할 경우, q가 입력될 때 while문을 종료합니다.

capture.release() # 메모리를 해제합니다.
cv2.destroyAllWindows() # 모든 윈도우창을 닫습니다.

# Tip : cv2.destroyWindow("윈도우 창 제목")을 이용하여 특정 윈도우 창만 닫을 수 있습니다.