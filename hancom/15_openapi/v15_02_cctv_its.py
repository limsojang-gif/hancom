import urllib.request
import urllib.parse
from urllib.error import HTTPError, URLError
import json
import pandas as pd

# 1. 기존 인증키 사용
key = "db5c00dc1fce45c49049bff225a0fea6"

# 2. API 요청 조건
params = {
    "apiKey": key,
    "type": "its",      # its: 일반도로 / ex: 고속도로
    "cctvType": 1,
    "minX": 126.0,
    "maxX": 129.0,
    "minY": 34.0,
    "maxY": 38.0,
    "getType": "json"
}

# 3. API 요청 URL 생성
url_cctv = (
    "https://openapi.its.go.kr:9443/cctvInfo?"
    + urllib.parse.urlencode(params)
)

try:
    # 4. API 요청
    with urllib.request.urlopen(url_cctv, timeout=20) as response:
        json_str = response.read().decode("utf-8")

    # 5. JSON 문자열을 딕셔너리로 변환
    json_object = json.loads(json_str)

    # 6. CCTV 데이터 가져오기
    data = json_object.get("response", {}).get("data", [])

    if not data:
        print("검색된 CCTV 데이터가 없습니다.")
        print("API 응답:", json_object)
        raise SystemExit

    # 7. 데이터프레임 생성
    cctv_play = pd.json_normalize(data)

    print(f"검색된 CCTV 수: {len(cctv_play)}")
    print("데이터 열:", cctv_play.columns.tolist())

    # 8. cctvurl 열 확인
    if "cctvurl" not in cctv_play.columns:
        print("응답 데이터에 cctvurl이 없습니다.")
        raise SystemExit

    # 9. 첫 번째 CCTV 선택
    test_url = cctv_play["cctvurl"].iloc[0]

    print("==============================")
    print(f"선택된 CCTV URL: {test_url}")

except HTTPError as error:
    print("HTTP 오류:", error.code, error.reason)

except URLError as error:
    print("네트워크 연결 오류:", error.reason)

except json.JSONDecodeError:
    print("API 응답을 JSON으로 변환하지 못했습니다.")

except Exception as error:
    print("오류 발생:", error)