from ultralytics import solutions
import cv2

# 1. 카메라 설정
stream_url = "http://210.99.70.120:1935/live/cctv001.stream/playlist.m3u8"
cap = cv2.VideoCapture(stream_url)
#cap = cv2.VideoCapture(0) - 내 웹캠

# 2. 히트맵 모델 로드
heatmap = solutions.Heatmap(
    model="yolo11n.pt",
    colormap=cv2.COLORMAP_MAGMA
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("못 읽음")
        break

    # 3-1. 누적 히트맵 갱신
    results = heatmap(frame)

    # 3-2. 결과 이미지 가져오기
    annotated_frame = results.plot_im

    # 3-3. 결과 화면 출력
    cv2.imshow("HEATMAP", annotated_frame)

    # 3-4. q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("q키를 눌러서 종료")
        break

# 4. 자원 해제
cap.release()
cv2.destroyAllWindows()