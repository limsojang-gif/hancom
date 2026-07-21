from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
stream_url = "http://210.99.70.120:1935/live/cctv001.stream/playlist.m3u8"
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("CCTV 스트림을 열 수 없습니다.")
    raise SystemExit

# 2. 거리 계산 객체 생성
# show=True: Ultralytics가 창과 마우스 이벤트를 자동으로 관리
distance = solutions.DistanceCalculation(
    model="yolo11n.pt",
    show=True
)

# 3. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("프레임 읽기 실패")
        break

    # 3-1. 객체 탐지 및 거리 계산
    results = distance.process(frame)

    # show=True이므로 cv2.imshow()는 작성하지 않음
    pixel_distance = results.pixels_distance

    # 3-2. 거리 상태 출력
    if pixel_distance is None or pixel_distance <= 0:
        print("[거리] ----px [상태] 객체 2개를 클릭하세요.")

    elif pixel_distance >= 150:
        status = "SAFE"
        print(f"[거리] {pixel_distance:.2f}px [상태] ==> {status}")

    elif pixel_distance >= 100:
        status = "WARNING"
        print(f"[거리] {pixel_distance:.2f}px [상태] ==> {status}")

    else:
        status = "DANGER"
        print(f"[거리] {pixel_distance:.2f}px [상태] ==> {status}")

    # 3-3. q 키로 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Q 키를 눌러서 종료합니다.")
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()