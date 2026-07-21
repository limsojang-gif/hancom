from ultralytics import solutions
import cv2


# 1. 비디오 경로 설정 
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv013.stream/playlist.m3u8")

# 2. 마우스 이벤트 처리 함수 정의 
points = []
def mouse_callback(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"클리된 좌표는{x, y}입니다")

# 3, 윈도우 창 설정 및 함수 등록 
cv2.namedWindow("GET_X_Y", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("GET_X_Y", mouse_callback)

# 4. 비디오 프레임 처리 
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("실패")
        break
# 4-1 프레임 사이즈 
    re_frame = cv2.resize(frame, (560, 480))    

    cv2.imshow("GET_X_Y", re_frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        print("Q 키를 눌러서 종료")
        break

# 5. 해제 

cap.release()
cv2.destroyAllWindows()

# 좌 상당 1번\
# 좌하단\
#  우하단
# 우상단