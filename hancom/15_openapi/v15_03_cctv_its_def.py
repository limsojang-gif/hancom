import urllib.request
import json
import pandas as pd
import cv2


# 1. CCTV URL을 가져오는 함수
def its_cctv(cctv_index=77):
    key = "db5c00dc1fce45c49049bff225a0fea6"

    Type = "its"
    getType = "json"

    minX, maxX = 120.95, 127.02
    minY, maxY = 30.55, 37.69

    # API 요청 URL 생성
    url_cctv = (
        f"https://openapi.its.go.kr:9443/cctvInfo"
        f"?apiKey={key}&type={Type}&cctvType=1"
        f"&minX={minX}&maxX={maxX}"
        f"&minY={minY}&maxY={maxY}"
        f"&getType={getType}"
    )

    # API 요청
    response = urllib.request.urlopen(url_cctv)
    json_str = response.read().decode("utf-8")

    # JSON → 딕셔너리 → 데이터프레임
    json_object = json.loads(json_str)
    cctv_play = pd.json_normalize(
        json_object["response"]["data"]
    )

    # 선택한 CCTV URL
    test_url = cctv_play["cctvurl"].iloc[cctv_index]

    print(f"선택된 CCTV URL: {test_url}")
    print(f"CCTV 번호: {cctv_index}")

    return test_url


# 2. 함수 실행: CCTV URL 받기
test_url = its_cctv(77)

# 3. CCTV 영상 열기
cap = cv2.VideoCapture(test_url)

if not cap.isOpened():
    print("CCTV 영상을 열 수 없습니다.")
    raise SystemExit

# 4. CCTV 영상 화면 출력
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("CCTV 프레임 읽기 실패")
        break

    cv2.imshow("ITS CCTV", frame)

    # q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("q 키를 눌러 종료합니다.")
        break

# 5. 자원 해제
cap.release()
cv2.destroyAllWindows()