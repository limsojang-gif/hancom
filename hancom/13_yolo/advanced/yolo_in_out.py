from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
stream_url = (
    "http://210.99.70.120:1935/live/"
    "cctv013.stream/playlist.m3u8"
)

cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("CCTV 스트림을 열 수 없습니다.")
    raise SystemExit

# 2. 카운팅 선 설정
count_points = [
    (196, 330),
    (191, 442),
    (512, 397),
    (408, 268)
]

# 3. 모델 로드 및 카운터 객체 생성
counter = solutions.ObjectCounter(
    model="yolo11n.pt",
    show=False,
    region=count_points
)

# 4. 프레임 처리
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("프레임 읽기 실패")
        break

    # 4-1. 프레임 크기 변경
    re_frame = cv2.resize(frame, (640, 480))

    # 4-2. 객체 탐지 및 IN/OUT 계산
    results = counter(re_frame)

    # 4-3. 처리된 프레임 표시
    cv2.imshow("IN/OUT COUNT", results.plot_im)

    # 카운트 결과 출력
    print(
        f"IN: {results.in_count}, "
        f"OUT: {results.out_count}"
    )

    # 4-4. q 키로 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("q를 눌러 종료합니다.")
        break

# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()
