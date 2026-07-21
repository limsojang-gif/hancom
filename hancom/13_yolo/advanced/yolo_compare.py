from ultralytics import YOLO
import cv2
import time

# 1. 모델 선택
#model = YOLO("yolo11n.pt")
model = YOLO("yolo11n_openvino_model")

# 2. 카메라 설정
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    raise SystemExit

# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("프레임 읽기 실패")
        break

    # 3-1. 추론 시간 측정
    start_time = time.perf_counter()
    results = model(frame, verbose=False)
    end_time = time.perf_counter()

    # 3-2. FPS 계산
    model_time = end_time - start_time

    if model_time > 0:
        fps = 1 / model_time
    else:
        fps = 0

    # 3-3. 결과 이미지 및 FPS 표시
    annotated_frame = results[0].plot()

    cv2.putText(
        annotated_frame,
        f"{fps:.1f} FPS",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("YOLO FPS", annotated_frame)

    # 3-4. q 키로 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("q 키를 눌러 종료합니다.")
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()