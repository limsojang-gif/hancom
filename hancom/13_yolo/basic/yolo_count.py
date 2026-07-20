from ultralytics import YOLO
import cv2

# 1. CCTV 스트리밍 URL 설정
stream_url = (
    "http://210.99.70.120:1935/live/"
    "cctv009.stream/playlist.m3u8"
)

cap = cv2.VideoCapture(stream_url)

# 2. YOLO 모델 로드
model = YOLO("yolo11n.pt")

# 3. 위험 기준
WARNING_THRESHOLD = 5

# 스트리밍 연결 확인
if not cap.isOpened():
    print("CCTV 스트리밍을 열 수 없습니다.")
    raise SystemExit

# 4. 실시간 프레임 처리
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("CCTV 영상을 읽지 못했습니다.")
        break

    # 4-1. YOLO 추론
    results = model(frame, verbose=False)

    # 4-2. 탐지 박스를 그린 프레임 생성
    annotated_frame = results[0].plot()

    # 4-3. 탐지 객체 수
    count = len(results[0].boxes)

    # 4-4. 상태 및 글자 색 결정
    if count >= WARNING_THRESHOLD:
        status = "Warning"
        color = (0, 0, 255)  # 빨간색
    else:
        status = "Normal"
        color = (0, 255, 0)  # 초록색

    # 4-5. 탐지 객체 수와 상태 표시
    cv2.putText(
        annotated_frame,
        f"Detected: {count}, {status}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2,
        cv2.LINE_AA
    )

    # 4-6. 영상 출력
    cv2.imshow("CCTV YOLO", annotated_frame)

    # 4-7. q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("q키 눌러서 종료합니다.")
        break

# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()
