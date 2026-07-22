from ultralytics import YOLO
import cv2

from v15_03_cctv_its_def import its_cctv


# 1. CCTV URL 가져오기
test_url = its_cctv(50)

# 2. CCTV 영상 열기
cap = cv2.VideoCapture(
    test_url,
    cv2.CAP_FFMPEG
)

if not cap.isOpened():
    print("CCTV 영상을 열 수 없습니다.")
    raise SystemExit

# 3. YOLO 모델 로드
model = YOLO("yolo11n.pt")

# 4. 출력 창 생성
cv2.namedWindow(
    "ITS_YOLO",
    cv2.WINDOW_AUTOSIZE
)

# 5. CCTV 프레임 처리
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("CCTV 프레임 읽기 실패")
        break

    # 5-1. YOLO 객체 탐지
    results = model(frame, verbose=False)

    # 5-2. 탐지 결과 화면 생성
    annotated_frame = results[0].plot()

    # 5-3. 화면 출력
    cv2.imshow("ITS_YOLO", annotated_frame)

    # 5-4. q 키로 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("q 키를 눌러 종료합니다.")
        break

# 6. 자원 해제
cap.release()
cv2.destroyAllWindows()