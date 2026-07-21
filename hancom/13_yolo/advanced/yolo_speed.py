from ultralytics import solutions
import cv2

# 1. 비디오 경로
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv013.stream/playlist.m3u8")

# 2. 속도 추천 객체 생성 & 모델로드 
yolo_speed = solutions.SpeedEstimator (
    model = "yolo11n.pt",
    show = False,
    classes=[2],
    line_width =2,        #바운딩 박스 선 두께
    max_speed=120,       #최대 속도 상한
    meter_per_pixel=0.5  #픽샐 1개 = 실제 0.5m 
)

# 3, 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 못읽었어 ")
        break

    # 3-1  속도 계산 및 추적 수행 \
    results = yolo_speed(frame)

    # 3-2 처리된 프레임 표시 
    cv2.imshow("speed", results.plot_im)

    # 3-3 q 종료
    if cv2.waitKey(1) &0xFF == ord('q'):
        print("q 눌러 해제")
        break

# 4. 자원 해제 
cap.release()
cv2.destroyAllWindows()